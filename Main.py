# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('bestsellers.csv')


# # Get the first 5 rows of the spreadsheet
# print(df.head())

# # Get the shape of the spreadsheet
# print(df.shape)

# # Get the column names of the spreadsheet
# print(df.columns)

# # Get summary statistics for each column
# print(df.describe())

# df.drop_duplicates(inplace=True)

# df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)


# df["Price"] = df["Price"].astype(float)

# author_counts = df['Author'].value_counts()
# print(author_counts)

# avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
# print(avg_rating_by_genre)


# # Export top selling authors to a CSV file
# author_counts.head(10).to_csv("top_authors.csv")

# # Export average rating by genre to a CSV file
# avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")


# # Plot author counts as a bar chart
# author_counts.head(10).plot(kind='bar', color='blue', title='Top 10 Authors by Book Count')
# plt.xlabel('Author')
# plt.ylabel('Book Count')
# plt.show()

# # Plot average rating by genre as a bar chart
# avg_rating_by_genre.plot(kind='bar', color='green', title='Average Rating by Genre')
# plt.xlabel('Genre')
# plt.ylabel('Average Rating')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('eu_entry_level_data_analyst_linkedin_jobs_sample.csv')

# Clean and preprocess the data
df.drop_duplicates(inplace=True)
df.rename(columns={"job_title": "Job Title", "contract": "Contract Type", "mode": "Work Mode", 
                   "city": "City", "country": "Country", "company": "Company", 
                   "sector": "Sector", "linkedin_skills": "Skills"}, inplace=True)

# Top 10 companies by the number of job postings
company_counts = df['Company'].value_counts()
top_10_companies = company_counts.head(10)

# Top 5 countries by the number of job postings
country_counts = df['Country'].value_counts()
top_5_countries = country_counts.head(5)

# Top 5 job titles by frequency
job_title_counts = df['Job Title'].value_counts()
top_5_job_titles = job_title_counts.head(5)

# Visualization

# Figure 1: Top 10 companies by the number of job postings (Bar Chart)
plt.figure(figsize=(12, 6))
top_10_companies.plot(kind='bar', color='blue', title='Top 10 Companies by Number of Job Postings')
plt.xlabel('Company')
plt.ylabel('Number of Job Postings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Figure 2: Top 5 countries by the number of job postings (Bar Chart)
plt.figure(figsize=(8, 5))
top_5_countries.plot(kind='bar', color='green', title='Top 5 Countries by Number of Job Postings')
plt.xlabel('Country')
plt.ylabel('Number of Job Postings')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Figure 3: Top 5 job titles by frequency (Bar Chart)
plt.figure(figsize=(8, 5))
top_5_job_titles.plot(kind='bar', color='orange', title='Top 5 Job Titles by Frequency')
plt.xlabel('Job Title')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()