import pandas as pd
import numpy as np
import json
import time
import datetime
from datetime import timedelta

# Python3 program to Grouping list 
# elements based on frequency
from collections import Counter
import itertools

#Build a feature of the text
#Import TF-IDF function
# TF: Term frequency
# IDF: Inverse Document Frequency
from sklearn.feature_extraction.text import TfidfVectorizer

#Compare similarity between the query and the description
#using cosine similarity, the degree of similarity is measured by comparing the angle between two vectors
from sklearn.metrics.pairwise import cosine_similarity

import plotly.express as px 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_pills import pills
# from streamlit_card import card
# from textwrap import wrap

df_jobs = pd.read_excel('linkedin_job_details.xlsx')
df_jobs = df_jobs.drop(['Unnamed: 0'], axis=1)
df_jobs['Job Skills'] = df_jobs['Job Skills'].fillna("[]")
df_jobs['Job Skills'] = [eval(skills) for skills in list(df_jobs['Job Skills'].values)]
df_jobs['Unlisted Skill'] = df_jobs['Unlisted Skill'].fillna("[]")
df_jobs['Unlisted Skill'] = [eval(skills) for skills in list(df_jobs['Unlisted Skill'].values)]
df_jobs['All Skills'] = df_jobs['Job Skills'] + df_jobs['Unlisted Skill']

df_skills = pd.read_excel('linkedin_job_skills.xlsx')
df_skills = df_skills.drop(['Unnamed: 0'], axis=1)

#
pills_job_title = ''
pills_job_skills = ''


# tfidf = TfidfVectorizer(stop_words='english')
# feature = tfidf.fit_transform(df_jobs['translated_en'])

def find_similar_jobs(filtered_df, search_text):
    if search_text.strip() == '':
        return filtered_df, list(filtered_df.index)

    tfidf = TfidfVectorizer(stop_words='english')
    feature = tfidf.fit_transform(filtered_df['translated_en'])

    query_feature = tfidf.transform([search_text])
    cosins = cosine_similarity(query_feature, feature).flatten()

    results = cosins.argsort()[::-1][:len([value for value in cosins if value > 0.0])]

    return filtered_df.filter(items = results, axis=0), results


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
# streamlit emojis: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# get icons at Bootstap Icons:  https://icons.getbootstrap.com/
st.set_page_config(page_title="What-The-Job", page_icon=":compass:", layout="wide")

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here: :mag:")

# Use a text_input to get the keywords to filter the dataframe
text_search = st.sidebar.text_input("Find keyword", value="")

selected_jobs = df_jobs

selected_jobs, sorted_jobs = find_similar_jobs(selected_jobs, text_search)

options = list(selected_jobs["Job Country"].unique())
options.insert(0, 'All')
location = st.sidebar.multiselect(
    ":globe_with_meridians: Location:",
    options=options,
    default=['All']
)
if 'All' in location:
    location = selected_jobs["Job Country"].unique()

options = list(selected_jobs["Job Title"].unique())
options.insert(0, 'All')
job_title = st.sidebar.multiselect(
    ":page_facing_up: Title:",
    options=options,
    default=['All']
)
if 'All' in job_title:
    job_title = selected_jobs["Job Title"].unique()

options = list(selected_jobs["Company Name"].unique())
options.insert(0, 'All')
company_name = st.sidebar.multiselect(
    ":office: Company:",
    options=options,
    default=['All']
)
if 'All' in company_name:
    company_name = selected_jobs["Company Name"].unique()

options = [value for value in df_jobs["Work Setting"].unique() if pd.isna(value) == False]
options.insert(0, 'All')
work_setting = st.sidebar.multiselect(
    ":computer: Remote Work Option:",
    options=options,
    default=['All']
)
if 'All' in work_setting:
    work_setting = selected_jobs["Work Setting"].unique()

options = [value for value in df_jobs["Experience Level"].unique() if pd.isna(value) == False]
options.insert(0, 'All')
post_experience = st.sidebar.multiselect(
    ":star2: Experience:",
    options=options,
    default=['All']
)
if 'All' in post_experience:
    post_experience = selected_jobs["Experience Level"].unique()

options = [value for value in df_jobs["Post Language"].unique() if pd.isna(value) == False]
options.insert(0, 'All')
post_language = st.sidebar.multiselect(
    ":books: Language:",
    options=options,
    default=['All']
)
if 'All' in post_language:
    post_language = selected_jobs["Post Language"].unique()

selected_jobs = selected_jobs.query(
    """`Job Country` in @location & `Job Title` in @job_title & `Company Name` in @company_name & `Work Setting` in @work_setting & `Experience Level` in @post_experience & `Post Language` in @post_language"""
)

# Check if the dataframe is empty:
if selected_jobs.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.

def show_text_card(label = '', font_size = '18px', alignment = 'left', color = 'white', font_weight = 'normal', line_spacing = '1.0'):
        text_card_display = f'''
                <p style="color:{color}; font-size: {font_size}; font-weight: {font_weight}; text-decoration:none; text-align: {alignment}; line-height:{line_spacing}">{label}</p>
        
        '''
        return text_card_display

# ---- MAINPAGE ----
st.title(":compass: What-The-Job App")
st.markdown("##")

# About page
with st.expander(label='''
                 -- About                                                                     -
                 ''', expanded=False):
    
    about_title_label = 'About'
    about_title_color = 'grey'
    about_title_font_size = '28px'
    about_title_font_weight = 'bold' 

    about_title_display = f'''
            <p style="color:{about_title_color}; font-size: {about_title_font_size}; font-weight: {about_title_font_weight}; text-decoration:none;">{about_title_label}</p>
        '''

    about_color = 'grey'
    about_font_size = '28px'
    about_font_weight = 'bold' 
    about_label_header = '''
                Ever wondered what skills are in demand for your dream role? Or maybe, you want to future-proof your career by getting upskilled for the next big role.
                '''
    about_label = '''
                This app aims to help find the top skills that are needed for the dream job and leverage the takeaway to update resumes when it's time to make the career leap.\n
                '''

    instruction_label_header = '''
                        How to use the app
                        '''
    instruction_label = '''
                        1. Enter a key phrase to find a particular job
                        '''
    
    st.markdown(show_text_card(label = about_label_header, font_weight='bold', font_size='20px'), unsafe_allow_html=True)
    # st.markdown('##')
    st.markdown(show_text_card(label = about_label, font_weight='normal', font_size='14px'), unsafe_allow_html=True)
    about_label = '''
            1. Find the top job titles in companies of your choice
            '''
    st.markdown(show_text_card(label = about_label, font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)
    about_label = '''
            2. Find out what skills are highly in-demand in a specialized industry
            '''
    st.markdown(show_text_card(label = about_label, font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)
    about_label = '''
            3. Find out which area of expertise to upskill before applying for a senior role
            '''
    st.markdown(show_text_card(label = about_label, font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)
    
    st.markdown('##')
    st.markdown(show_text_card(label = instruction_label_header, font_weight='bold', font_size='20px'), unsafe_allow_html=True)
    st.markdown(show_text_card(label = instruction_label, font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)
    instruction_label = '''
                    2. Filter by location, job title, company, experience level, work setting, and even language of job description
                    '''
    st.markdown(show_text_card(label = instruction_label, font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)

    st.markdown('##')
    st.markdown(show_text_card(label = 'Developer note', font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)
    st.markdown(show_text_card(label = 'This app was developed independently. Made for desktop browsers', font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)
    st.markdown(show_text_card(label = '- Developed by: Naim Zahari', font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)
    st.markdown(show_text_card(label = '- Based in Berlin, Germany', font_weight='normal', font_size='14px', line_spacing=0.5), unsafe_allow_html=True)
    linked_profile_display = f'<a href = "https://www.linkedin.com/in/naimiskandar22/"><p style="color:grey; font-size: 14px; text-decoration:none; line-height:0.5">:link: Find me on LinkedIn</p></a>'
    st.markdown(linked_profile_display, unsafe_allow_html=True)
    st.markdown('##')
    # st.markdown(body=''':link:[Find me on LinkedIn] (https://www.linkedin.com/in/naimiskandar22/)''')

st.markdown("##")

# horizontal menu
# get icons at Bootstap Icons:  https://icons.getbootstrap.com/
selected_menu = option_menu(menu_title = None,
                            options = ["Home", "Job Posts", "Skillframe", "Salary"],
                            icons = ['house', 'bookmark-star-fill', 'calendar-range-fill', 'cash-stack'],
                            menu_icon = 'cast',
                            default_index=0,
                            orientation='horizontal')
# option_menu(menu_title = None,
#                             options = ["Home", "Job Posts", "Map"],
#                             icons = ['house', 'bookmark-star-fill', 'map'],
#                             menu_icon = 'cast',
#                             default_index=0,
#                             orientation='horizontal')


# Top Skills
combined_listed_skill_lists = list(itertools.chain.from_iterable(selected_jobs['Job Skills'].values))
listed_skills_grouped = list(zip(Counter(combined_listed_skill_lists).keys(), Counter(combined_listed_skill_lists).values()))

combined_unlisted_skill_lists = list(itertools.chain.from_iterable(selected_jobs['Unlisted Skill'].values))
unlisted_skills_grouped = list(zip(Counter(combined_unlisted_skill_lists).keys(), Counter(combined_unlisted_skill_lists).values()))

skills = list(set([listed_skills_grouped[n][0] for n in range(len(listed_skills_grouped))] + [unlisted_skills_grouped[n][0] for n in range(len(unlisted_skills_grouped))]))
df_top_skills = pd.DataFrame([], columns = ['Skill Name', 'Listed frequency', 'Unlisted frequency', 'Total'])
for skill in skills:
    dict_entry = {}
    listed_freq = sum([row[1] for row in listed_skills_grouped if row[0] == skill])
    unlisted_freq = sum([row[1] for row in unlisted_skills_grouped if row[0] == skill])

    dict_entry['Skill Name'] = skill
    dict_entry['Listed frequency'] = listed_freq
    dict_entry['Unlisted frequency'] = unlisted_freq
    dict_entry['Total'] = listed_freq + unlisted_freq

    df_top_skills = pd.concat([df_top_skills, pd.DataFrame([dict_entry])], ignore_index=True)
    df_top_skills.reset_index()

# pills(label: str, 
    # options: Iterable[str], 
    # icons: Iterable[str] = None, 
    # index: Optional[int] = 0, *, 
    # format_func: Callable = None, 
    # label_visibility: str = 'visible', 
    # clearable: bool = None, 
    # key: str = None)
def get_keyword_pills(df, skills_df):
    keyword_dict = {}
    x_skills_to_sort = skills_df.sort_values(by=['Total'], ascending = False)['Total']
    y_skills_to_sort = skills_df.sort_values(by=['Total'], ascending = False)['Skill Name']

    for row in range(0,20):
        if row < len(list(df['Job Title'].value_counts().index)):
            keyword_dict[list(df['Job Title'].value_counts().index)[row]] = df['Job Title'].value_counts()[row]
        if row < len(list(df['Company Name'].value_counts().index)):
            if list(df['Company Name'].value_counts().index)[row] is not None:
                keyword_dict[list(df['Company Name'].value_counts().index)[row]] = df['Company Name'].value_counts()[row]
        if row < len(list(df['Industry'].value_counts().index)):
            if list(df['Industry'].value_counts().index)[row] is not None:
                keyword_dict[list(df['Industry'].value_counts().index)[row]] = df['Industry'].value_counts()[row]
        if row < len(x_skills_to_sort):
            keyword_dict[y_skills_to_sort[row]] = x_skills_to_sort[row]

    sorted_keywords = sorted(keyword_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_keywords = [key[0] for key in sorted_keywords]
    keyword_limit = 18
    if len(sorted_keywords) < keyword_limit:
        keyword_limit = len(sorted_keywords)
    sorted_keywords = sorted_keywords[:keyword_limit]

    briefcase_icon = "💼"
    pushpin_icon = "📌"
    page_icon = "📄"
    industry_icon = "📎"
    circle_icon = "🟢"

    icon_list = []
    for keyword in sorted_keywords:
        if keyword in list(df['Job Title'].values):
            icon_list.append(page_icon)
        elif keyword in list(df['Company Name'].values):
            icon_list.append(briefcase_icon)
        elif keyword in y_skills_to_sort:
            icon_list.append(pushpin_icon)
        elif keyword in list(df['Industry'].values):
            icon_list.append(industry_icon)
        else:
            icon_list.append(pushpin_icon)

    return sorted_keywords, icon_list, y_skills_to_sort

keywords, icons, common_skills = get_keyword_pills(selected_jobs, df_top_skills)
if len(keywords) > 0:
    selected_pills = pills(label = "Keywords", options = keywords, icons = icons, clearable= True)

if selected_pills is not None:
    if selected_pills in list(selected_jobs['Job Title'].values):
        selected_jobs = selected_jobs[selected_jobs['Job Title'] == selected_pills]
    elif selected_pills in list(selected_jobs['Company Name'].values):
        selected_jobs = selected_jobs[selected_jobs['Company Name'] == selected_pills]
    elif selected_pills in list(selected_jobs['Industry'].values):
        selected_jobs = selected_jobs[selected_jobs['Industry'] == selected_pills]
    elif selected_pills in common_skills:
        selected_jobs = selected_jobs[selected_pills in list(selected_jobs['Job Skills'].values)]

combined_listed_skill_lists = list(itertools.chain.from_iterable(selected_jobs['Job Skills'].values))
listed_skills_grouped = list(zip(Counter(combined_listed_skill_lists).keys(), Counter(combined_listed_skill_lists).values()))

combined_unlisted_skill_lists = list(itertools.chain.from_iterable(selected_jobs['Unlisted Skill'].values))
unlisted_skills_grouped = list(zip(Counter(combined_unlisted_skill_lists).keys(), Counter(combined_unlisted_skill_lists).values()))

skills = list(set([listed_skills_grouped[n][0] for n in range(len(listed_skills_grouped))] + [unlisted_skills_grouped[n][0] for n in range(len(unlisted_skills_grouped))]))
df_top_skills = pd.DataFrame([], columns = ['Skill Name', 'Listed frequency', 'Unlisted frequency', 'Total'])
for skill in skills:
    dict_entry = {}
    listed_freq = sum([row[1] for row in listed_skills_grouped if row[0] == skill])
    unlisted_freq = sum([row[1] for row in unlisted_skills_grouped if row[0] == skill])

    dict_entry['Skill Name'] = skill
    dict_entry['Listed frequency'] = listed_freq
    dict_entry['Unlisted frequency'] = unlisted_freq
    dict_entry['Total'] = listed_freq + unlisted_freq

    df_top_skills = pd.concat([df_top_skills, pd.DataFrame([dict_entry])], ignore_index=True)
    df_top_skills.reset_index()

st.markdown("""---""")

if selected_menu == 'Home':
    st.title('Home')
    st.markdown('##')

    # Top scorecards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(show_text_card(label = "Jobs Found", font_size='32px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
        st.markdown(show_text_card(label = len(selected_jobs['Job ID'].unique()), font_size='24px', alignment='center'), unsafe_allow_html=True)
    with col2:
        st.markdown(show_text_card(label = "Companies", font_size='32px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
        st.markdown(show_text_card(label = len(selected_jobs['Company Name'].unique()), font_size='24px', alignment='center'), unsafe_allow_html=True)
        # st.markdown("Companies")
        # st.metric("", len(selected_jobs['Company Name'].unique()))
    with col3:
        st.markdown(show_text_card(label = "Industries", font_size='32px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
        st.markdown(show_text_card(label = len(selected_jobs['Industry'].unique()), font_size='24px', alignment='center'), unsafe_allow_html=True)
        # st.markdown("Industries")
        # st.metric("", len(selected_jobs['Industry'].unique()))

    st.markdown('---')

    with st.container(border=False, height=500):
        highlight_col1, highlight_col2 = st.columns(2)
        with highlight_col1:
            # get icons at Bootstap Icons:  https://icons.getbootstrap.com/
            selected_highlights_menu = option_menu(menu_title = None,
                                        options = ["Job Titles", "Companies", "Industry", "Experience Level", "Skills"],
                                        icons = ['1-square', '2-square', '3-square', '4-square', '5-square'],
                                        menu_icon = 'cast',
                                        default_index=0,
                                        orientation='vertical')
        with highlight_col2:
            if selected_highlights_menu == 'Job Titles':
                plot_values = list(selected_jobs['Job Title'].value_counts())[:3]
                plot_labels = list(selected_jobs['Job Title'].value_counts().index)[:3]
                max_label_char = 18
                plot_labels = [(l[:max_label_char]+'...') if (len(l) > max_label_char) else l for l in plot_labels]

                first_value = plot_values[0]
                first_label = plot_labels[0]

                if len(plot_values) > 1:
                    first_value = plot_values[0]
                    first_label = plot_labels[0]
                    second_value = plot_values[1]
                    second_label = plot_labels[1]

                    plot_values[0] = second_value
                    plot_labels[0] = second_label
                    plot_values[1] = first_value
                    plot_labels[1] = first_label

                fig_top_jobs = px.bar(
                    selected_jobs,
                    x=plot_values,
                    y=plot_labels,
                    orientation="h",
                    # title="<b>Top Titles</b>",
                    color_discrete_sequence=["#0083B8"] * 5,
                    template="plotly_white"
                )
                # fig_top_jobs.update_layout(yaxis={'categoryorder':'total ascending'})
                fig_top_jobs.update_xaxes(title='Total', visible=True, showticklabels=True)
                fig_top_jobs.update_yaxes(title='', visible=True, showticklabels=True)
                if len(plot_values) > 1:
                    fig_top_jobs.add_annotation(text="⭐", x = first_value + 1, y=1, showarrow=False)
                st.plotly_chart(fig_top_jobs, use_container_width=True)
            elif selected_highlights_menu == 'Companies':
                plot_values = list(selected_jobs['Company Name'].value_counts())[:3]
                plot_labels = list(selected_jobs['Company Name'].value_counts().index)[:3]
                max_label_char = 18
                plot_labels = [(l[:max_label_char]+'...') if (len(l) > max_label_char) else l for l in plot_labels]

                first_value = plot_values[0]
                first_label = plot_labels[0]

                if len(plot_values) > 1:
                    first_value = plot_values[0]
                    first_label = plot_labels[0]
                    second_value = plot_values[1]
                    second_label = plot_labels[1]

                    plot_values[0] = second_value
                    plot_labels[0] = second_label
                    plot_values[1] = first_value
                    plot_labels[1] = first_label

                fig_top_companies = px.bar(
                    selected_jobs,
                    x=plot_values,
                    y=plot_labels,
                    orientation="h",
                    # title="<b>Top Titles</b>",
                    color_discrete_sequence=["#0083B8"] * 5,
                    template="plotly_white"
                )
                # fig_top_jobs.update_layout(yaxis={'categoryorder':'total ascending'})
                fig_top_companies.update_xaxes(title='Total', visible=True, showticklabels=True)
                fig_top_companies.update_yaxes(title='', visible=True, showticklabels=True)
                if len(plot_values) > 1:
                    fig_top_companies.add_annotation(text="⭐", x = first_value + 1, y=1, showarrow=False)
                st.plotly_chart(fig_top_companies, use_container_width=True)
            elif selected_highlights_menu == 'Industry':
                if (len(list(selected_jobs['Industry'].value_counts().index)) >= 1) | (len(selected_jobs['Industry'].value_counts().index) > 0):
                    plot_values = list(selected_jobs['Industry'].value_counts())[:3]
                    plot_labels = list(selected_jobs['Industry'].value_counts().index)[:3]
                    max_label_char = 18
                    plot_labels = [(l[:max_label_char]+'...') if (len(l) > max_label_char) else l for l in plot_labels]

                    first_value = plot_values[0]
                    first_label = plot_labels[0]

                    if len(plot_values) > 1:
                        first_value = plot_values[0]
                        first_label = plot_labels[0]
                        second_value = plot_values[1]
                        second_label = plot_labels[1]

                        plot_values[0] = second_value
                        plot_labels[0] = second_label
                        plot_values[1] = first_value
                        plot_labels[1] = first_label

                    fig_top_industries = px.bar(
                        selected_jobs,
                        x=plot_values,
                        y=plot_labels,
                        orientation="h",
                        # title="<b>Top Titles</b>",
                        color_discrete_sequence=["#0083B8"] * 5,
                        template="plotly_white"
                    )
                    # fig_top_jobs.update_layout(yaxis={'categoryorder':'total ascending'})
                    fig_top_industries.update_xaxes(title='Total', visible=True, showticklabels=True)
                    fig_top_industries.update_yaxes(title='', visible=True, showticklabels=True)
                    if len(plot_values) > 1:
                        fig_top_industries.add_annotation(text="⭐", x = first_value + 1, y=1, showarrow=False)
                    st.plotly_chart(fig_top_industries, use_container_width=True)
            elif selected_highlights_menu == 'Experience Level':
                if (len(list(selected_jobs['Industry'].value_counts().index)) >= 1) | (len(selected_jobs['Industry'].value_counts().index) > 0):
                    plot_values = list(selected_jobs['Experience Level'].value_counts())[:3]
                    plot_labels = list(selected_jobs['Experience Level'].value_counts().index)[:3]
                    max_label_char = 18
                    plot_labels = [(l[:max_label_char]+'...') if (len(l) > max_label_char) else l for l in plot_labels]

                    first_value = plot_values[0]
                    first_label = plot_labels[0]

                    if len(plot_values) > 1:
                        first_value = plot_values[0]
                        first_label = plot_labels[0]
                        second_value = plot_values[1]
                        second_label = plot_labels[1]

                        plot_values[0] = second_value
                        plot_labels[0] = second_label
                        plot_values[1] = first_value
                        plot_labels[1] = first_label

                    fig_top_seniorities = px.bar(
                        selected_jobs,
                        x=plot_values,
                        y=plot_labels,
                        orientation="h",
                        # title="<b>Top Titles</b>",
                        color_discrete_sequence=["#0083B8"] * 5,
                        template="plotly_white"
                    )
                    # fig_top_jobs.update_layout(yaxis={'categoryorder':'total ascending'})
                    fig_top_seniorities.update_xaxes(title='Total', visible=True, showticklabels=True)
                    fig_top_seniorities.update_yaxes(title='', visible=True, showticklabels=True)
                    if len(plot_values) > 1:
                        fig_top_seniorities.add_annotation(text="⭐", x = first_value + 1, y=1, showarrow=False)
                    st.plotly_chart(fig_top_seniorities, use_container_width=True)
            elif selected_highlights_menu == 'Skills':
                skills_to_sort = df_top_skills.copy()
                
                plot_values = list(skills_to_sort.sort_values(by=['Total'], ascending = False)['Total'])[:3]
                plot_labels = list(skills_to_sort.sort_values(by=['Total'], ascending = False)['Skill Name'])[:3]
                max_label_char = 18
                plot_labels = [(l[:max_label_char]+'...') if (len(l) > max_label_char) else l for l in plot_labels]

                first_value = plot_values[0]
                first_label = plot_labels[0]

                if len(plot_values) > 1:
                    first_value = plot_values[0]
                    first_label = plot_labels[0]
                    second_value = plot_values[1]
                    second_label = plot_labels[1]

                    plot_values[0] = second_value
                    plot_labels[0] = second_label
                    plot_values[1] = first_value
                    plot_labels[1] = first_label

                fig_top_skills = px.bar(
                    skills_to_sort,
                    x=plot_values,
                    y=plot_labels,
                    orientation="h",
                    # title="<b>Top Titles</b>",
                    color_discrete_sequence=["#0083B8"] * 5,
                    template="plotly_white"
                )
                # fig_top_skills.update_layout(yaxis={'categoryorder':'total ascending'})
                fig_top_skills.update_xaxes(title='Total', visible=True, showticklabels=True)
                fig_top_skills.update_yaxes(title='', visible=True, showticklabels=True)
                if len(plot_values) > 1:
                    fig_top_skills.add_annotation(text="⭐", x = first_value + 1, y=1, showarrow=False)
                st.plotly_chart(fig_top_skills, use_container_width=True)

    st.markdown("""---""")

    selected_demands_menu = option_menu(menu_title = None,
                            options = ["Titles", "Skills"],
                            icons = ['house', 'bookmark-star-fill'],
                            menu_icon = 'cast',
                            default_index=0,
                            orientation='horizontal')
    
    if selected_demands_menu == 'Titles':
        with st.container(border = False, height=1200):
            
            # Top Titles
            pill_index = 0
            title_chart_starting_index = 0
            title_chart_last_index = 5
            plot_values = list(selected_jobs['Job Title'].value_counts())
            plot_labels = list(selected_jobs['Job Title'].value_counts().index)

            col1, col2, col3 = st.columns(3)

            with col2:
                pill_index = st.slider("Job Rank #", 1, len(plot_labels)+1, 1)
            pill_index=pill_index-1
            
            titlecard_col1, titlecard_col2, titlecard_col3 = st.columns(3)
            with titlecard_col1:
                st.markdown(show_text_card(label = plot_labels[pill_index], font_size='24px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
            with titlecard_col2:
                st.markdown(show_text_card(label = "🏆 Rank #", font_size='32px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
                st.markdown(show_text_card(label = (pill_index+1), font_size='24px', alignment='center'), unsafe_allow_html=True)
            with titlecard_col3:
                st.markdown(show_text_card(label = "Found", font_size='32px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
                st.markdown(show_text_card(label = (str(plot_values[pill_index]) + ' times'), font_size='24px', alignment='center'), unsafe_allow_html=True)

            title_chart_starting_index = (0 if pill_index - 2 <= 0 else (len(plot_labels)-5 if (len(plot_labels) - pill_index) <0 else pill_index-2))
            title_chart_last_index = (title_chart_starting_index + 5) + (pill_index + 3 - len(plot_labels) if pill_index + 3 > len(plot_labels) else 0)

            max_label_char = 18
            plot_labels = [(l[:max_label_char]+'...') if (len(l) > max_label_char) else l for l in plot_labels]
            
            fig_top_titles = px.bar(
                selected_jobs,
                x=plot_labels[title_chart_starting_index:title_chart_last_index],
                y=plot_values[title_chart_starting_index:title_chart_last_index],
                orientation="v",
                # title="<b>Top Titles</b>",
                color_discrete_sequence=["#0083B8"] * 5,
                template="plotly_white"
            )
            # fig_top_titles.update_layout(yaxis={'categoryorder':'total ascending'})
            fig_top_titles.update_xaxes(title='', visible=True, showticklabels=True)
            fig_top_titles.update_yaxes(title='Total', visible=True, showticklabels=True)
            st.plotly_chart(fig_top_titles, use_container_width=True)

            st.markdown("""---""")

            min_len = len(plot_values)
            max_len = min_len
            if max_len > 20:
                max_len = 20
            if min_len >= 5: 
                pills_curr_job = pills(label = "Job Titles", options = plot_labels[:max_len], clearable= True)
                pills_job_title = pills_curr_job
    elif selected_demands_menu == 'Skills':
        with st.container(border = False, height=1200):
            # Top Skills
            skills_to_sort = df_top_skills.copy()

            pill_index = 0
            skill_chart_starting_index = 0
            skill_chart_last_index = 5
            plot_values = list(skills_to_sort.sort_values(by=['Total'], ascending = False)['Total'])
            plot_labels = list(skills_to_sort.sort_values(by=['Total'], ascending = False)['Skill Name'])
            
            col1, col2, col3 = st.columns(3)

            with col2:
                pill_index = st.slider("Skill Rank #", 1, len(list(skills_to_sort['Skill Name'].unique()))+1, 1)
            pill_index=pill_index-1
            
            skillcard_col1, skillcard_col2, skillcard_col3 = st.columns(3)
            with skillcard_col1:
                st.markdown(show_text_card(label = plot_labels[pill_index], font_size='24px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
            with skillcard_col2:
                st.markdown(show_text_card(label = "🏆 Rank #", font_size='32px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
                st.markdown(show_text_card(label = (pill_index+1), font_size='24px', alignment='center'), unsafe_allow_html=True)
            with skillcard_col3:
                st.markdown(show_text_card(label = "Found", font_size='32px', alignment='center', font_weight='bold'), unsafe_allow_html=True)
                st.markdown(show_text_card(label = (str(plot_values[pill_index]) + ' times'), font_size='24px', alignment='center'), unsafe_allow_html=True)

            skill_chart_starting_index = (0 if pill_index - 2 <= 0 else (len(plot_labels)-5 if (len(plot_labels) - pill_index) <0 else pill_index-2))
            skill_chart_last_index = (skill_chart_starting_index + 5) + (pill_index + 3 - len(plot_labels) if pill_index + 3 > len(plot_labels) else 0)

            max_label_char = 18
            plot_labels = [(l[:max_label_char]+'...') if (len(l) > max_label_char) else l for l in plot_labels]

            fig_top_skills_2 = px.bar(
                skills_to_sort,
                x=plot_labels[skill_chart_starting_index:skill_chart_last_index],
                y=plot_values[skill_chart_starting_index:skill_chart_last_index],
                orientation="v",
                # title="<b>Top Titles</b>",
                color_discrete_sequence=["#0083B8"] * 5,
                template="plotly_white"
            )
            # fig_top_skills.update_layout(yaxis={'categoryorder':'total ascending'})
            fig_top_skills_2.update_xaxes(title='', visible=True, showticklabels=True)
            fig_top_skills_2.update_yaxes(title='Total', visible=True, showticklabels=True)
            st.plotly_chart(fig_top_skills_2, use_container_width=True)

            st.markdown("""---""")

            min_len = len(list(skills_to_sort.sort_values(by=['Total'], ascending = False)['Skill Name']))
            max_len = min_len
            if max_len > 20:
                max_len = 20
            if min_len >= 5:
                pills(label = "Skills", options = list(skills_to_sort.sort_values(by=['Total'], ascending = False)['Skill Name'])[:max_len], clearable= True)

elif selected_menu == 'Job Posts':
    st.title('Job Posts')
    st.markdown('##')

    cards_limit = 30
    curr_card = 0
    columns_to_create = 1
    st_rows = [st.columns(columns_to_create) for card_row in range(int(cards_limit/columns_to_create)+1)]

    for row in st_rows:
        for col in row:
            if curr_card < len(selected_jobs):
                # if sorted_jobs[curr_card] not in list(selected_jobs.index):
                #     continue

                tile = col.container()

                # tile.write(f'{sorted_jobs[curr_card]} + {len(selected_jobs)}')

                # df_index_to_show = selected_jobs.index[sorted_jobs[curr_card]]
                df_index_to_show = selected_jobs.index[curr_card]
                selected_jobs_row = selected_jobs.loc[df_index_to_show]

                # tile.write(df_index_to_show)
                # job_card_style = '''
                #     wrapText: true; autoHeight: true
                # '''
                # title_display = f'<p style="color:white; text-decoration:none; font-size:45px; wrapText: true;">{selected_jobs_row["Job Title"]}</p>'
                # company_display = f'<p style="color:white; text-decoration:none; font-size:16px; wrapText: true;">{selected_jobs_row["Company Name"]}</p>'
                # tile.markdown(title_display)
                # tile.markdown(company_display)
                # tile.markdown(selected_jobs_row['Experience Level'])
                
                # title_display = f'<p style="color:white; font-size: 18px; font-weight: bold; text-decoration:none">{selected_jobs_row["Job Title"]}</p>'
                # tile.markdown(title_display, unsafe_allow_html=True)
                tile.markdown(show_text_card(label=selected_jobs_row["Job Title"], color='white', font_weight='bold'), unsafe_allow_html=True)
                if selected_jobs_row["Company Name"] is not None:
                    # company_display = f'<p style="color:white; font-size: 12px; text-decoration:none; line-height:0.5">{selected_jobs_row["Company Name"]}</p>'
                    # tile.markdown(company_display, unsafe_allow_html=True)
                    tile.markdown(show_text_card(label=selected_jobs_row["Company Name"], color='white', font_size='12px', line_spacing=0.5), unsafe_allow_html=True)
                if type(selected_jobs_row['Job Country']) == str:
                    # location_display = f'<p style="color:white; font-size: 12px; text-decoration:none; line-height:0.5">{selected_jobs_row["Job Country"]}</p>'
                    # tile.markdown(location_display, unsafe_allow_html=True)
                    tile.markdown(show_text_card(label=selected_jobs_row["Job Country"], color='white', font_size='12px', line_spacing=0.5), unsafe_allow_html=True)
                if type(selected_jobs_row["Top Card Details"]) == str:
                    # topcard_display = f'<p style="color:white; font-size: 12px; text-decoration:none; line-height:0.5">{" · ".join(eval(selected_jobs_row["Top Card Details"]))}</p>'
                    # tile.markdown(topcard_display, unsafe_allow_html=True)
                    tile.markdown(show_text_card(label=(" · ".join(eval(selected_jobs_row["Top Card Details"]))), color='white', font_size='12px', line_spacing=0.5), unsafe_allow_html=True)
                if type(selected_jobs_row["Job Link"]) == str:
                    url = selected_jobs_row['Job Link']
                    # tile.write(f"[:link: Go to LinkedIn page]({url})", unsafe_allow_html=False)
                    topcard_display = f'<a href = {url}><p style="color:white; font-size: 14px; text-decoration:none; line-height:0.5">:link: Go to LinkedIn page</p></a>'
                    tile.markdown(topcard_display, unsafe_allow_html=True)
                
                date_post = selected_jobs_row["Post Date"]
                if type(selected_jobs_row["Post Date"]) == float:
                    date_post = datetime.datetime.fromtimestamp(selected_jobs_row["Post Date"]).strftime('%Y-%m-%d')
                
                tile.markdown(show_text_card(label=("\n[Saved at: "+date_post+']'), color='white', font_size='12px', line_spacing=0.5), unsafe_allow_html=True)

                

                tile.markdown("""---""")

                # change_link_color = """
                #         <style>
                #         .link_style {
                #         color: green;
                #         background-color: transparent;
                #         text-decoration: none;
                #         } LinkedIn Page
                #         </style>
                #         """
                # change_link_color = """
                #         <style>
                #          {
                #         color: green;
                #         background-color: transparent;
                #         text-decoration: none;
                #         } LinkedIn Page
                #         </style>
                #         """
                # font-family: 'Roboto', sans-serif; 
                # font-size: 18px;
                # font-weight: 500;
                # color: #091747;
                # new_title = f'<a href = {url}><p style="font-family:sans-serif; color:white; font-size: 15px; text-decoration:none;">New image</p></a>'
                # tile.markdown(new_title, unsafe_allow_html=True)
                # tile.markdown('<p style="font-size: 10px;">Hello World</p>')
                # tile.markdown(change_link_color, unsafe_allow_html=True)

                curr_card = curr_card + 1
elif selected_menu == 'Skillframe':
    st.title('Skills Over Time')
    st.markdown('##')

    # get icons at Bootstap Icons:  https://icons.getbootstrap.com/
    skills_page_display = option_menu(menu_title = None,
                            options = ["Demands", "Company", "Experience Level"],
                            icons = ['1-square', '2-square', '3-square'],
                            menu_icon = 'cast',
                            default_index=0,
                            orientation='horizontal')
    
    skillframe_col1, skillframe_col2, skillframe_col3, skillframe_col4 = st.columns(4)

    demands_skillframe = []
    company_skillframe = []
    country_skillframe = []
    experience_skillframe = []
    duration_skillframe = ['All time', 'Last 1 year', 'Last 2 years']
    selected_experience_skillframe = 0
    selected_duration_skillframe = 0

    
    with skillframe_col1:
        options = list(selected_jobs["Job Country"].unique())
        options.insert(0, 'All')
        country_skillframe = st.multiselect(
            ":office: Company:",
            options=options,
            default=['All'],
            key='country_skillframe_key'
        )
        if 'All' in country_skillframe:
            country_skillframe = selected_jobs["Job Country"].unique()  

    with skillframe_col2:
        options = list(selected_jobs["Company Name"].unique())
        options.insert(0, 'All')
        company_skillframe = st.multiselect(
            ":office: Company:",
            options=options,
            default=['All'],
            key='company_skillframe_key'
        )
        if 'All' in company_skillframe:
            company_skillframe = selected_jobs["Company Name"].unique()

    with skillframe_col3:
        options = [value for value in df_jobs["Experience Level"].unique() if pd.isna(value) == False]
        options.insert(0, 'All')
        experience_skillframe = st.selectbox(
            ":star2: Experience:",
            options=options,
            index=0,
            key='experience_skillframe_key'
        )
        if experience_skillframe == 'All':
            experience_skillframe = selected_jobs["Experience Level"].unique()

    with skillframe_col4:
        options = ['All time', 'Last 1 year', 'Last 2 years']
        duration_skillframe = st.selectbox(
            ":calendar: Date:",
            options=options,
            index=0,
            key='duration_skillframe_key'
        )

    skills_to_sort = df_top_skills.copy()
    sorted_skill_labels = list(skills_to_sort.sort_values(by=['Total'], ascending = False)['Skill Name'])
    options = sorted_skill_labels

    if skills_page_display == 'Demands':
        options.insert(0, 'All')
        demands_skillframe = st.multiselect(
            ":toolbox: Skills:",
            options=options,
            default=options[1:6]
        )
        if 'All' in demands_skillframe:
            demands_skillframe = sorted_skill_labels
    else:
        demands_skillframe = st.selectbox(
            ":toolbox: Skills:",
            options=options,
            index=0,
            key='demands_skillframe_key'
        )
        demands_skillframe = [demands_skillframe]


    # skillframe_page_jobs = selected_jobs.copy()
    skillframe_page_jobs = selected_jobs.query(
            """`Job Country` in @country_skillframe & `Company Name` in @company_skillframe & `Experience Level` in @experience_skillframe"""
        )
    
    skillframe_start_date = None
    
    if duration_skillframe == 'All time':
        skillframe_start_date = None
    elif duration_skillframe == 'Last 1 year':
        skillframe_start_date = datetime.date.today() - datetime.timedelta(days=365)
    elif duration_skillframe == 'Last 2 years':
        skillframe_start_date = datetime.date.today() - datetime.timedelta(days=730)

    if skillframe_start_date is not None:
        skillframe_page_jobs = skillframe_page_jobs[(skillframe_page_jobs['Post Date'] >= skillframe_start_date) & (skillframe_page_jobs['Post Date'] <= datetime.date.today())]
    
    skillframe_df1 = pd.DataFrame([
        [p] + a for P, *a in skillframe_page_jobs[['All Skills', 'Job ID', 'Post Date', 'Company Name', 'Experience Level']].values
        for p in P
    ], columns=[['Skills', 'Job ID', 'Post Date', 'Company Name', 'Experience Level']])

    skillframe_df1['YY-MM'] = skillframe_df1['Post Date']
    skillframe_df1['Total'] = 1
    for index in skillframe_df1.index:
        job_row = skillframe_df1.loc[index]
        date_post = job_row["Post Date"]
        if type(date_post) == float:
            date_post = datetime.datetime.fromtimestamp(date_post).strftime('%Y-%m-%d')
        # job_row['Post Date'] = datetime.datetime.fromtimestamp(date_post).strftime('%Y-%m-%d')
        date_post = datetime.datetime.strptime(date_post, '%Y-%m-%d').date()
        job_row['Post Date'] = date_post
        job_row['YY-MM'] = str(date_post)[:7]
        skillframe_df1.loc[index] = job_row
    skillframe_df1.reset_index()
    skillframe_df1.columns = skillframe_df1.columns.get_level_values(0)
    
    skillframe_df_pivotted = None

    # skillframe_df_pivotted = pd.pivot_table(skillframe_df1, values='Total', index=['YY-MM'], columns=['Company Name', 'Skills'], aggfunc=np.sum)
    if skills_page_display == 'Demands':
        skillframe_df_pivotted = pd.pivot_table(skillframe_df1, values='Total', index=['YY-MM'], columns='Skills', aggfunc=np.sum)
        # skillframe_df_pivotted.columns = skillframe_df_pivotted.columns.get_level_values(1)
        skillframe_df_pivotted = skillframe_df_pivotted[demands_skillframe]
    elif skills_page_display == 'Company':
        skillframe_df_pivotted = pd.pivot_table(skillframe_df1, values='Total', index=['YY-MM'], columns='Company Name', aggfunc=np.sum)
        # skillframe_df_pivotted.columns = skillframe_df_pivotted.columns.get_level_values(0)
        # skillframe_df_pivotted = skillframe_df_pivotted[demands_skillframe]
    elif skills_page_display == 'Experience Level':
        skillframe_df_pivotted = pd.pivot_table(skillframe_df1, values='Total', index=['YY-MM'], columns='Experience Level', aggfunc=np.sum)
    
    fig = go.Figure()
    for col in skillframe_df_pivotted.columns:
        fig.add_trace(go.Scatter(x=skillframe_df_pivotted.index, y=skillframe_df_pivotted[col].values,
                                name = col,
                                mode = 'markers+lines',
                                line=dict(shape='linear'),
                                connectgaps=True
                                )
                    )

    st.plotly_chart(fig, use_container_width=True)

elif selected_menu == 'Salary':
    st.title('Pay Range')
    st.markdown('##')

    salary_col1, salary_col2, salary_col3, salary_col4 = st.columns(4)

    demands_salary = []
    company_salary = []
    country_salary = []
    experience_salary = []
    duration_salary = ['All time', 'Last 1 year', 'Last 2 years']

    with salary_col1:
        options = list(selected_jobs[selected_jobs['Pay Salary'].notna()]["Job Country"].unique())
        options.insert(0, 'All')
        country_salary = st.multiselect(
            ":globe_with_meridians: Country:",
            options=options,
            default=['All'],
            key='country_salary_key'
        )
        if 'All' in country_salary:
            country_salary = selected_jobs["Job Country"].unique()
    
    with salary_col2:
        options = list(selected_jobs[selected_jobs['Pay Salary'].notna()]["Company Name"].unique())
        options.insert(0, 'All')
        company_salary = st.multiselect(
            ":office: Company:",
            options=options,
            default=['All'],
            key='company_salary_key'
        )
        if 'All' in company_salary:
            company_salary = selected_jobs["Company Name"].unique()

    with salary_col3:
        options = [value for value in selected_jobs[selected_jobs['Pay Salary'].notna()]["Experience Level"].unique() if pd.isna(value) == False]
        options.insert(0, 'All')
        experience_salary = st.multiselect(
            ":star2: Experience:",
            options=options,
            default=['All'],
            key='experience_salary_key'
        )
        if 'All' in experience_salary:
            experience_salary = selected_jobs["Experience Level"].unique()

    with salary_col4:
        options = ['All time', 'Last 1 year', 'Last 2 years']
        selected_duration_salary = st.selectbox(
            ":calendar: Date:",
            options=options,
            index=0,
            key='duration_salary_key'
        )

    # salary_page_jobs = selected_jobs.copy()
    salary_page_jobs = selected_jobs.query(
            """`Job Country` in @country_salary & `Company Name` in @company_salary & `Experience Level` in @experience_salary"""
        )
    
    salary_start_date = None
    
    if selected_duration_salary == 'All time':
        salary_start_date = None
    elif selected_duration_salary == 'Last 1 year':
        salary_start_date = datetime.date.today() - datetime.timedelta(days=365)
    elif selected_duration_salary == 'Last 2 years':
        salary_start_date = datetime.date.today() - datetime.timedelta(days=730)

    if salary_start_date is not None:
        salary_page_jobs = salary_page_jobs[(salary_page_jobs['Post Date'] >= salary_start_date) & (salary_page_jobs['Post Date'] <= datetime.date.today())]

    salary_df_columns = ['Job ID', 'Job Title', 'Company Name', 'Experience Level', 'Experience in Years', 'Pay Salary', 'Min (Range)', 'Max (Range)', 'AVG (Range)', 'Salary (Bucket)']
    salary_df = pd.DataFrame([], columns = salary_df_columns)

    for index in salary_page_jobs.index:
        job_row = salary_page_jobs.loc[index]

        if job_row['Pay Salary'] is None:
            continue

        salary_range_min = None
        try:
            salary_range_min = str(job_row['Pay Salary']).split(' - ')[0]
            salary_range_min = float(str(salary_range_min).replace('/yr', ''))
        except:
            salary_range_min = None
        
        salary_range_max = None
        try:
            salary_range_max = str(job_row['Pay Salary']).split(' - ')[1]
            salary_range_max = float(str(salary_range_max).replace('/yr', ''))
        except:
            salary_range_max = None

        salary_dict = {}

        salary_dict['Job ID'] = job_row["Job ID"]
        salary_dict['Job Title'] = job_row["Job Title"]
        salary_dict['Company Name'] = job_row["Company Name"]
        salary_dict['Experience Level'] = job_row["Experience Level"]
        salary_dict['Experience in Years'] = float(job_row["Experience in Years"])
        salary_dict['Pay Salary'] = str(job_row["Pay Salary"])
        salary_dict['Min (Range)'] = salary_range_min
        salary_dict['Max (Range)'] = salary_range_max
        salary_dict['AVG (Range)'] = np.average([value for value in [salary_range_min, salary_range_max] if value is not None])

        if salary_range_min is None:
            salary_dict['Salary (Bucket)'] = None
            salary_df = pd.concat([salary_df, pd.DataFrame([salary_dict])], ignore_index=True)
        elif salary_range_max is None:
            salary_dict['Salary (Bucket)'] = salary_range_min
            salary_df = pd.concat([salary_df, pd.DataFrame([salary_dict])], ignore_index=True)
        elif salary_range_max is not None:
            salary_interval = 10000
            for interval_index in range(0, int((round(salary_range_max, -4)-round(salary_range_min, -4))/salary_interval)+1):
                salary_dict['Salary (Bucket)'] = round(salary_range_min, -4) + salary_interval*interval_index
                salary_df = pd.concat([salary_df, pd.DataFrame([salary_dict])], ignore_index=True)

        salary_df.reset_index()

    fig = go.Figure()
    fig = px.histogram(salary_df, x="Salary (Bucket)", color = "Experience Level", barmode = "overlay")
    st.plotly_chart(fig, use_container_width=True)
