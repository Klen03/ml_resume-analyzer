import pandas as pd

# Load the raw data
df = pd.read_csv("datasets/raw_data/recruitment_data.csv")

# Inspect the first few rows
print("\nPreview of data:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Map numerical categories to labels
gender_map = {0: "Female", 1: "Male"}
education_map = {1: "High School", 2: "Bachelor", 3: "Master", 4: "PhD"}
strategy_map = {1: "Referral", 2: "Online", 3: "Agency"}

df["Gender"] = df["Gender"].map(gender_map)
df["EducationLevel"] = df["EducationLevel"].map(education_map)
df["RecruitmentStrategy"] = df["RecruitmentStrategy"].map(strategy_map)

 # Save clean data to processed_data file
df.to_csv("datasets/processed_data/cleaned_recruitment_data.csv", index=False)