# Define common programming languages and ML keywors to search for
from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd
from cleaning import clean_text

# Cleaning recruitment_data.csv
df = pd.read_csv("datasets/processed_data/cleaned_updated_resume_dataset.csv")

programming_keywords = [
    "python", "java", "c++", "c#", "javascript", "sql", "r", "scala",
    "matlab", "html", "css", "typescript", "bash", "shell"
]

ml_keywords = [
    "regression", "svm", "naive bayes", "knn", "random forest", "decision trees",
    "boosting", "clustering", "word embedding", "sentiment analysis",
    "nlp", "dimensionality reduction", "topic modeling", "lda", "nmf", "pca",
    "neural networks", "deep learning"
]

# Function to count keywords from resumes
def count_keywords_from_text(resumes, keyword_list):
    counter = Counter()
    for resume in resumes:
        text = clean_text(resume).lower()
        for keyword in keyword_list:
            if keyword in text:
                counter[keyword] += 1
    return counter.most_common(10)

# App;ly the broader keyword-based counting
top_langs_keywords = count_keywords_from_text(df['Resume'].dropna(), programming_keywords)
top_ml_keywords = count_keywords_from_text(df['Resume'].dropna(), ml_keywords)

# Plot updated: Top Programming Languages (keyword-based)
langs, counts = zip(*top_langs_keywords)
plt.figure(figsize=(10,5))
plt.bar(langs, counts)
plt.title("Top Programming Languages (Keyword-Based)")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
lang_img_path ="datasets/visuals_images/top_programming_languages.png"
plt.savefig(lang_img_path)
plt.close()

# Plot updated: Top Machine Learning Skills (keyword-based)
mls, ml_counts = zip(*top_ml_keywords)
plt.figure(figsize=(10, 5))
plt.bar(mls, ml_counts)
plt.title("Top Machine Learning Skills (Keyword-Based)")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
ml_img_path = "datasets/visuals_images/top_machine_learning_skills.png"
plt.savefig(ml_img_path)
plt.close()

lang_img_path, ml_img_path