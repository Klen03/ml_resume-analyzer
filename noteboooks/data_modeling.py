from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import os
import numpy as np
from sentence_transformers import SentenceTransformer

# Load cleaned dataset
df_cleaned = pd.read_csv("datasets/processed_data/cleaned_updated_resume_dataset.csv")

# Define features and target
X = df_cleaned['Resume'].fillna('')
y = df_cleaned['Category']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Vectorize resumes using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

accuracy, report

# Convert classification report to a DataFrame and save as CSV
report_df = pd.DataFrame(report).transpose()

# Save to CSV
report_csv_path = "datasets/results/updated_resume_classification_report_.csv"
report_df.to_csv(report_csv_path, index=True)

report_csv_path

# Load BERT model for sentence embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Embed the resumes
X_train_emb = model.encode(X_train.tolist(), show_progress_bar=True)
X_test_emb = model.encode(X_test.tolist(), show_process_bar=True)

# Train a classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_emb, y_train)

# Evaluate
y_pred = clf.predict(X_test_emb)
print(classification_report(y_test, y_pred))
