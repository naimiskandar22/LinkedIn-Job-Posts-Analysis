# LinkedIn-Job-Posts-Analysis

## Released App:
- Developed with Python and Streamlit
- Published on Streamlit Community Server
- Website at https://career-top-skills-nz.streamlit.app/

## Gallery
<details> 
 <summary> Website gallery </summary>

 ## Website Front Page: Home
 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/698d6be5-139a-4914-a6e1-57206e4ce92b) 
 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/1f69322c-cd95-4274-99e4-2243ddf5a98b) 
 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/bcfd162e-113e-4ffa-bc0f-8ff4c2c62ddc)
 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/908e09ae-3068-4427-a4bd-9eb27b3d66ad)
 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/21ad1592-25c0-4170-afe7-3312d9f23da8)
 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/975bba4e-2b50-4e07-a31f-15672de399ea)
 ## Page: LinkedIn Job Posts
 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/42d5d5dd-bbcc-49fb-93a8-05de8de70fce)

</details>

## Objective:
- Build a general understanding of the job market for data-related jobs based on job posts on LinkedIn
- Provide an easy-to-use platform that shows insights on the job market, particularly job titles, companies, industries and associated skills

## How To Use The Project:
- You need a Jupyter notebook, and an environment with packages listed in the requirements.txt file to run the Python scripts

## Challenges:
- Although web scraping is legal, LinkedIn does not welcome web scraping on the platform
- LinkedIn has placed mechanics on the platform to prevent web crawling robots by flagging suspicious activites and providing arbitrary naming in most of the HTML headers
- There is not a LinkedIn API that allows developers to get information of posts on LinkedIn Jobs

## UML Diagrams

<details>
 <summary> Diagrams </summary>


UML Use Case Diagram
![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/c565c5cd-e135-49e6-9145-c67f319c7d08)

UML Class Diagram
![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/9632c844-9645-4dd4-a9b9-10def5806eed)

</details>

## Domain Driven Design (DDD)

<details>

 <summary> Domain Model </summary>

The domain model illustrates the entities relevant to the end-to-end process from gathering information to exploratory data analysis (EDA) to displaying the analysis on a published website

![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/429ef382-a869-455f-b397-3d8971b9f888)

As stated in the one of the challenges, LinkedIn takes measures to make web scraping difficult and inaccessible to web crawler agents. Nevertheless, Job posts on LinkedIn have similar patterns to how text information are shown and the text information can be obtained as long as the right serialized identification classes are determined. The information can be gathered for the following entities:
1. Source platform (LinkedIn)
   a. Job ID
   b. Post url link
   c. Reposted
   d. List status
   e. Company ID
2. Job details
   a. Job title
   b. Job description
   c. Language
   d. Experience level
   e. Location
   f. Industry
   g. Employment type
   h. Associated skills
3. Company
   a. Company name
   b. Company page link
   c. Industry
   d. Company size
   e. Company description

</details>

<details>

 <summary> Core Domain </summary>

To fulfill the main objective of the website, the most common job titles and associated job skills to job posts are primary indications to measure the benchmarks for generalized or specialized job options. A relatively substantial amount of records would provide an insightful overview of the job market and LinkedIn is a resourceful platform to gather information on available work at a given time. 

![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/f7528319-654e-4311-8422-2691e584e2e8)

As shown in the website gallery above, the website front page indicates the most common job title and the top skills associated to the job posts. Practicality and ease-of-use are the primary focus to provide the most impact for the users. Free tools such as Jobscan and Skillsyncer are useful to show ATS scores for resumes, however there are no free tools that show insights on job titles and top skills. This website provides a one-stop platform for users who are:
- Looking to update their resumes for general purposes
- Tailoring their resumes for specialized positions
- Determining the next skills to develop for senior positions

</details>

<details>

 <summary> Core Domain Chart </summary>

The core purpose of the website is to provide valuable information on the demanded job options on the market and democratize the feature to be available to the data community

![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/aa99903c-d398-4896-8d20-8a24bdf62da2)

The feature to display the insights mentioned multiple times on a published website is the determined minimum-viable product (MVP), however the website utilization and application lies on the exploratory data analysis processes that produces the insight shown. The exploratory data analysis processes include:
- Most common job titles
- Companies with the most job posts
- Top Industries from the job posts
- Top skills associated to the job posts
- Determine unlisted skills on the posts but were mentioned in the job description
- Extensive filter options on the website
- 

While the core feature is fundamental to the website, there are opportunities for further features that could be developed to enrich the website. Referring to an illustration from the DDD-crew, secondary features can be organized into different quadrants of viability to determine the impact and measured against the cost of the development. As elegantly illustrated in the picture below, features grouped as the Low Hanging Fruit on the bottom right box would provide the best return-on-investment (ROI) whereas the grey box on the top left is the least lucrative feature to develop.

![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/d9d9c199-1d2a-45a5-b520-950817e2db77)

Future expansions can be considered to provide higher value for the website. However, the impediments should always be considered to measure the potential ROI and committing to the feature development. Hence, the groupings can be described as follows:

<b>Low Hanging Fruit</b>
1. Trend Analysis
   - Advantage: Showing the highly demanded job titles and skills over time
   - Disadvantage: No significant obstructions, as this feature requires expanding upon the available analysis on the website

<b>Risk Averse</b>
1. Recommendation Chatbot
   - Advantage: It provides narrower or more relevant sorted searched jobs for users
   - Disadvantage: Could be computationally costly for the website, and broader or expansive data would be needed to drive maximum value
2. Forecasting Model
   - Advantage: Forecasting highly demanded jobs and skills for future jobs in the market
   - Disadvantage: Accuracy in forecasting model may be skewed when broader data is not available for model training

<b>Last Toothpaste in the Tube</b>
1. Automated Data Fetch
   - Advantage: Broader data can be obtained automatically for long-term period with minimal manual process
   - Disadvantage: LinkedIn has intuitive countermeasures to prevent suspected web crawlers or robots from fetching data on the platform, and there is no job posts API available to free users


</details>

<details>

 <summary> Ubiquitous Language </summary>

In the Domain-Driven Design process, ubiquitous language helps to align the relevant individuals in getting familiarized with the common terminologies used for the project development and getting a common understanding on the terminologies used in the project lifecycle.

The main terminologies and the description in the project are as follows:
- <b>Home Page</b>: Front page of the website where the insights are shown
- <b>Job Posts Page</b>: Second page of the website that shows the list of job posts gathered on LinkedIn
- <b>Top Job Title</b>: 3 most common job titles in the analysis output
- <b>Top Companies</b>: 3 most common companies in the analysis output
- <b>Top Industries</b>: 3 most common industries in the analysis output
- <b>Top Experience Levels</b>: 3 most common experience levels in the analysis output
- <b>Top Skills</b>: 3 most common associated skills to the jobs in the analysis output
- <b>Remote Work Options</b>: Remote options in the LinkedIn filter options. The listed options found on LinkedIn are On-site, Hybrid and Remote
- <b>Experience Levels</b>: Assigned experience level for the job posts on LinkedIn and is among one of the filter parameters. The listed experience levels found on LinkedIn include Entry level, Mid-Senior level, Internship, Contract, Part-time and Director

</details>

## Metrics

<details>

 <summary> Metrics </summary>




</details>

## Clean Code Development

<details>

 <summary> Explanation </summary>

Clean codes and general best practices are foundational to the project lifecycle, as easily readable codes are critical in facilitating or orchestrating continuous development of feature expansion. In that spirit, areas such as clear naming, unrepetitive functions and concise comments are included in the development code to allow changes when improvements are called for and to demonstrate the awareness of clean code development.

</details>

<details>

 <summary> Examples </summary>

To 

<details_ccc> 
 <summary> Example 1 </summary>
</details_ccc>

<details_ccc> 
 <summary> Example 1 </summary>
</details_ccc>

<details_ccc> 
 <summary> Example 1 </summary>
</details_ccc>

<details_ccc> 
 <summary> Example 1 </summary>
</details_ccc>

<details_ccc> 
 <summary> Example 1 </summary>
</details_ccc>

</details>
