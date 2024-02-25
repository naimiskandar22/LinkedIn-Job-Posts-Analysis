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
 - Job ID
 - Post url link
 - Reposted
 - List status
 - Company ID
2. Job details
 - Job title
 - Job description
 - Language
 - Experience level
 - Location
 - Industry
 - Employment type
 - Associated skills
3. Company
 - Company name
 - Company page link
 - Industry
 - Company size
 - Company description

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
- Text recommender by keyword search with scikit-learn's TFIDF

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

 <summary> General Practice </summary>

 - <b>Naming Variables and Functions</b>: Variables and functions have to be named concisely and appropriately.
   - Booleans: If any, boolean variables would be named with the prefix 'is', and followed by the purpose of the variable. For example, is_home_selected or is_done
   - Strings and Float (Numeric): If any, variables are named in singular form and the naming should be concise.
   - Lists and Dataframes: Variables are named in plural form
 - <b>Variable Naming Convention</b>: Naming convention of variables use snake case. Snake case (stylized as snake_case) is the naming convention in which each space is replaced with an underscore (_) character, and words are written in lowercase. For example, files_df and files_df_columns
 - <b>Function Naming Convention</b>: Naming convention of variables use pascal case. Pascal case is a naming convention where the first letter in every word is capitalized and the rest is in lowercase. For example, GetJobPostingID() and GetJobTitle()
 - <b>Unique Naming</b>: Definitions of new variables and functions should be named appropriately. Each variable should be used for specific purposes and there should not be more than 1 uses for specified variables. However, the variable values can be freely modified
 - <b>Comments</b>: Comments added are used to provide a clear descriptions. When necessary, comments should be included directly above the definitions of variables or functions.
 - <b>Functional Programming</b>: Identify instances where hard-coding can be avoided as much as possible. Rather than using hard-coded solutions, build functions to compute the solutions from identifiable patterns and return results with no side effects. If results cannot be found, return null and allow the code to move forward without being impeded.

</details>

<details>

 <summary> Examples </summary>

Find the examples of clean code development below.

<details> 
 <summary> Example 1 </summary>

Use case: Including comments to describe functions
Source file: job_analysis.ipynb

![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/e84c78bc-2c25-4bc2-893d-3f22c9d52731)

 
</details>

<details> 
 <summary> Example 2 </summary>

 Use case: Naming convention of functions (Pascal Case)
 Source file: job_analysis.ipynb

 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/e84c78bc-2c25-4bc2-893d-3f22c9d52731)

</details>

<details> 
 <summary> Example 3 </summary>
 
 Use case: Naming convention of list and dataframe (Snake Case)
 Source file: job_analysis.ipynb

 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/8322c6be-4bd3-498d-9ae7-32d1c1ce16f5)
 
</details>

<details> 
 <summary> Example 4 </summary>
 
 Use case: Functional programming, where a function is defined with parameters and returning value(s). If the attempt to get value(s) is unsuccessful, return null and the rest of the code still persists
 Source file: job_analysis.ipynb

 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/67c56a80-62df-4dac-b966-9e9d51fb9ff6)

</details>

<details> 
 <summary> Example 5 </summary>
 
 Use case: List and dataframe variables are given unique namings. Besides that, the namings are concise and appropriate to the specific purposes.
 Source file: job_analysis.ipynb

 ![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/e4e4ef75-2a34-470a-84fa-990fe89b9f88)

</details>

</details>

## Build Management System

<details>

 <summary> Metrics </summary>




</details>

## Unit Tests

<details>

 <summary> Explanation </summary>

In the jobs_analysis_test.ipynb file, the Python <b>assert</b> keyword is used to test if the function returns an expected value. Referring to the screenshot below, the <b>id_key</b> is hard-coded to get the job title in the post from the HTML text. However, the <b>id_key</b> in other job post pages on LinkedIn are arbitrary and applying the <b>id_key</b> manually is not acceptable. With the earlier defined function <b>diveHtmlTags()</b>, the job title can be obtained regardless of the arbitrary <b>id_key</b>. The same solution applies to obtain the other information on LinkedIn Job Post pages.

When the notebook cells with the <b>assert</b> keyword run successfully, the tests are successful and no <b>AssertionError</b> are triggered.

![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/0090c8b6-6a59-4bdc-b32a-3771e94bbda9)


</details>

## Continuous Delivery

<details>

 <summary> Explanation </summary>


</details>

## IDE

<details>

 <summary> Explanation </summary>


</details>


## DSL

<details>

 <summary> Explanation </summary>


</details>


## Functional Programming

<details>

 <summary> Explanation </summary>

The final data structure is defined and stored in a dataframe. Once the data has been processed and stored in a dataframe, the dataframe will be saved in an excel file. Hence, defining the dataframe columns and the required information are fundamental to the project outcome. As mentioned in the Clean Code Development general practice, functions with parameters and return values are critical to processing the required information with little room for hard-coded solutions. Regardless of the outcome of the implemented functions in the code, the code should persist and run successfully.

Refer to the screenshots below for the defined dataframes to be stored in excel files.

### Job Details Structure
![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/ffca5c50-5bcc-446b-8b82-2571c384c774)
### Top Skills Structure
![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/ffdcda45-9514-434a-a58a-c49bb06695b2)


</details>
