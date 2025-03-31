from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# Load your cleaned dataset
df = pd.read_csv("cleaned_updated_resume_dataset.csv")
X = df["Resume"].fillna("")
y = df["Category"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Load BERT model for sentence embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Embed the resumes
X_train_emb = model.encode(X_train.tolist(), show_progress_bar=True)
X_test_emb = model.encode(X_test.tolist(), show_progress_bar=True)

# Train a classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_emb, y_train)

# Evaluate
y_pred = clf.predict(X_test_emb)
print(classification_report(y_test, y_pred))