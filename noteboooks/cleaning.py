import pandas as pd
import re

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


def clean_text(text):
    """Fix encoding issues and normalize whitespace."""
    text = text.encode('latin1').decode('utf-8', errors='ignore')
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    return text.strip()

def extract_section(pattern, text):
    """Extracts section based on a pattern."""
    if not isinstance(text, str):
        return "Not specified"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "Not specified"

# Prepare cleaned data storage
cleaned_data = []

df = pd.read_csv("datasets/raw_data/UpdatedResumeDataSet.csv", encoding='utf-8-sig')

df['Resume'] = df['Resume'].fillna('').astype(str)

# Process each resume
for _, row in df.iterrows():
    category = row['Category']
    resume = row['Resume']

    # Extract common sections using simple heuristics
    prog_langs = extract_section(r'Programming Languages:\s*([^*]*)', resume)
    ml_skills = extract_section(r'Machine learning[:\-]*\s*([^*]*)', resume)
    db_viz = extract_section(r'Database(?:s)?(?: & Visualization)?[:\-]*\s*([^*]*)', resume)
    other_tools = extract_section(r'Others[:\-]*\s*([^*]*)', resume)
    education = extract_section(r'Education Details\s*[:\-]*\s*(.*?)(?=\s*Company Details|\s*Experience|\s*Skill Details|\s*$)', resume)
    job_title = extract_section(r'(?:Job\s+Title|Position)[:\-]*\s*(.*?)(?=\s*Company|\s*$)', resume)
    company = extract_section(r'Company[:\-]*\s*(.*?)(?=\s*Description|\s*$)', resume)
    job_desc = extract_section(r'Description[:\-]*\s*(.*?)(?=\s*Tools|$)', resume)
    tools = extract_section(r'Tools & Technologies[:\-]*\s*(.*)', resume)

    cleaned_data.append({
        "Category": category,
        "Programming Languages": prog_langs,
        "Machine Learning": ml_skills,
        "Databases & Visualization": db_viz,
        "Other Tools": other_tools,
        "Education": education,
        "Job Title": job_title,
        "Company": company,
        "Job Description": job_desc,
        "Tools & Technologies": tools,
    })

# Create a cleaned DataFrame
df_cleaned = pd.DataFrame(cleaned_data)

# Save to CSV
output_path = "datasets/processed_data/Cleaned_Resume_DataSet.csv"
df_cleaned.to_csv(output_path, index=False)

output_path