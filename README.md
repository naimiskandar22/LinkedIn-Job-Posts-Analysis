# LinkedIn-Job-Posts-Analysis

## Released App:
- Developed with Python and Streamlit
- Published on Streamlit Community Server
- Website at https://career-top-skills-nz.streamlit.app/

<details> 
 <summary> Website gallery </summary>

 ## Website Front Page: Analysis
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

While the core feature is fundamental to the website, there are opportunities for further features that could be developed to enrich the website. Referring to an illustration from the DDD-crew, secondary features can be organized into different quadrants of viability to determine the impact and measured against the cost of the development. As elegantly illustrated in the picture below, features grouped as the Low Hanging Fruit on the bottom right box would provide the best return-on-investment (ROI) whereas the grey box on the top left is the least lucrative feature to develop.

![image](https://github.com/naimiskandar22/LinkedIn-Job-Posts-Analysis/assets/29110245/0de70b7a-e7da-4865-a37c-10db090ee799)



</details>

