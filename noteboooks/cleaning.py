import pandas as pd

# Cleaning recruitment_data.csv
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



# Cleaning job_data.csv
df = pd.read_csv("datasets/raw_data/job_data.csv")

# Drop unnecessary columns
df = df.drop(columns=["Unnamed: 0"])

# Clean the description field
# These are stored as strings of lists (e.g., "['text']", with newline and extra symbols)
df["description"] = (
    df["description"]
    .astype(str)
    .str.replace(r"^\[|\]$", "", regex=True)  # remove starting/ending brackets
    .str.replace("', '", " ", regex=False)    # merge list items into one string
    .str.replace("'", "", regex=False)        # remove stray quotes
    .str.strip()
)

# Standardize text fields
text_cols = ["major_job", "job", "position", "location", "description"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

# Drop duplicates if any
df = df.drop_duplicates()

# Preview cleaned data
print(df.head())

# Step 7: Save cleaned version
df.to_csv("datasets/processed_data/cleaned_job_data.csv", index=False)