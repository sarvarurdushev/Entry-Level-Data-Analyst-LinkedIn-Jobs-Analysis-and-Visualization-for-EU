# Entry-Level-Data-Analyst-LinkedIn-Jobs-Analysis-and-Visualization-for-EU
This project analyzes a dataset of entry-level data analyst job postings in Europe collected from LinkedIn. The analysis identifies top hiring companies, countries with the most opportunities, and the most common job titles for data analysts. The results are visualized using bar charts for easy interpretation.
📁 Dataset
The dataset used is eu_entry_level_data_analyst_linkedin_jobs_sample.csv. It includes columns such as:

job_title

contract

mode

city

country

company

sector

linkedin_skills

### 🧼 Data Cleaning and Preprocessing
We begin by importing necessary libraries and cleaning the dataset.
```
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('eu_entry_level_data_analyst_linkedin_jobs_sample.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Rename columns for better readability
df.rename(columns={
    "job_title": "Job Title",
    "contract": "Contract Type",
    "mode": "Work Mode",
    "city": "City",
    "country": "Country",
    "company": "Company",
    "sector": "Sector",
    "linkedin_skills": "Skills"
}, inplace=True)
```
### 📈 Data Analysis
We explore the dataset by finding the top companies, countries, and job titles.

# Top 10 companies by job postings 
```
company_counts = df['Company'].value_counts()
top_10_companies = company_counts.head(10)
```
# Top 5 countries by job postings
```
country_counts = df['Country'].value_counts()
top_5_countries = country_counts.head(5)
```
# Top 5 job titles by frequency
```
job_title_counts = df['Job Title'].value_counts()
top_5_job_titles = job_title_counts.head(5)
```
### 📊 Data Visualization
🔹 Figure 1: Top 10 Companies by Number of Job Postings
```
plt.figure(figsize=(12, 6))
top_10_companies.plot(kind='bar', color='blue', title='Top 10 Companies by Number of Job Postings')
plt.xlabel('Company')
plt.ylabel('Number of Job Postings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```
🔹 Figure 2: Top 5 Countries by Number of Job Postings
```
plt.figure(figsize=(8, 5))
top_5_countries.plot(kind='bar', color='green', title='Top 5 Countries by Number of Job Postings')
plt.xlabel('Country')
plt.ylabel('Number of Job Postings')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```
🔹 Figure 3: Top 5 Job Titles by Frequency
```
plt.figure(figsize=(8, 5))
top_5_job_titles.plot(kind='bar', color='orange', title='Top 5 Job Titles by Frequency')
plt.xlabel('Job Title')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```
### ✅ Conclusion
This project gives insights into the most active employers, job markets, and role types for entry-level data analysts in Europe. It can be useful for job seekers to understand trends and plan applications accordingly.

🛠 Requirements
Python 3.x

pandas

matplotlib

Install required libraries using:
```
pip install pandas matplotlib
```
