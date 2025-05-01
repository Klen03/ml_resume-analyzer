import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import ast
import os

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
file_path = os.path.expanduser('datasets/processed_data/jobss_cleaned.csv')
df = pd.read_csv(file_path)


df['Key Skills'] = df['Key Skills'].str.split('|')
df['Functional Area'] = df['Functional Area'].str.split(' , ')
df['Industry'] = df['Industry'].str.split(' , ')

all_skills = [skill.strip().lower() for sublist in df['Key Skills'].dropna() for skill in sublist]

# 1. Job Role Distribution
plt.figure(figsize=(14, 8))
role_counts = df['Role'].value_counts().head(10)
sns.barplot(x=role_counts.values, y=role_counts.index, palette='viridis')
plt.title('Top 10 Most Common Job Roles')
plt.xlabel('Count')
plt.ylabel('Job Role')
plt.tight_layout()
plt.show()

# 2. Experience Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Min Experience'], bins=15, kde=True, color='skyblue')
plt.title('Distribution of Minimum Experience Requirements')
plt.xlabel('Years of Experience')
plt.ylabel('Number of Jobs')
plt.show()

# 3. Industry Distribution
# I "exploded" the industry lists to count properly
industries = df.explode('Industry')['Industry'].str.strip()
top_industries = industries.value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_industries.values, y=top_industries.index, palette='magma')
plt.title('Top 10 Industries with Most Job Openings')
plt.xlabel('Count')
plt.ylabel('Industry')
plt.tight_layout()
plt.show()

#4 Top Skills Word Cloud (requires wordcloud package)
top_skills = pd.Series(all_skills).value_counts().head(15)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_skills.values, y=top_skills.index, palette='plasma')
plt.title('Top 15 Most Required Skills')
plt.xlabel('Count')
plt.ylabel('Skill')
plt.tight_layout()
plt.show()

#5 Experience vs Role Category
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Min Experience', y='Role Category', palette='Set2')
plt.title('Experience Requirements by Role Category')
plt.tight_layout()
plt.show()

#6 Bar chart of Functional Areas
plt.figure(figsize=(12, 6))
func_areas = df.explode('Functional Area')['Functional Area'].str.strip()
func_area_counts = func_areas.value_counts().head(10)
sns.barplot(x=func_area_counts.values, y=func_area_counts.index, palette='Spectral')
plt.title('Top 10 Functional Areas')
plt.xlabel('Count')
plt.tight_layout()
plt.show()

#7 Number of Skills Required vs. Experience Level
df['Skill Count'] = df['Key Skills'].apply(lambda x: len(x) if isinstance(x, list) else 0)
plt.figure(figsize=(12, 6))
sns.boxplot(
    data=df,
    x='Min Experience',
    y='Skill Count',
    hue='Min Experience',
    palette='coolwarm',
    legend=False
)
plt.title('Number of Skills Required vs. Experience Level')
plt.xlabel('Minimum Experience (Years)')
plt.ylabel('Number of Skills Listed')
plt.tight_layout()
plt.show()


#8 Top 3 Skills Required for Top 10 Job Roles
top_roles = df['Role'].value_counts().head(10).index.tolist()
role_skills = df[df['Role'].isin(top_roles)].explode('Key Skills')
role_skills['Key Skills'] = role_skills['Key Skills'].str.strip().str.lower()

top_skills_per_role = (
    role_skills.groupby('Role')['Key Skills']
    .apply(lambda x: x.value_counts().head(3))
    .reset_index()
    .rename(columns={'level_1': 'Skill', 'Key Skills': 'Count'})
)
plt.figure(figsize=(14, 10))
sns.barplot(
    data=top_skills_per_role,
    x='Count',
    y='Role',
    hue='Skill',
    palette='tab20',
    dodge=False
)
plt.title('Top 3 Skills Required for Top 10 Job Roles')
plt.xlabel('Frequency')
plt.ylabel('Job Role')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()