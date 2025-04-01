# CS506 Project - Hiring Intelligence Dashboard
Our project reimagines resume analysis by shifting focus from vague AI suggestions to data-driven insights based on real hiring outcomes. Rather than trying to predict job offers directly, we analyze which resume traits most strongly correlate with success—using actual recruitment data, SHAP interpretability, and behavioral scoring. Our tool empowers job seekers not just with feedback, but with explanations and comparisons, allowing them to simulate changes, view trait benchmarks against successful applicants, and identify potential bias or inequality in the hiring process. We aim to move beyond generative feedback and toward transparent, evidence-backed recommendations. This provides applicants with quantifiable and context-aware recommendations instead of generic keyword tips.

## Project description:

By using **Natural Language Processing (NLP), machine learning models, and statistical analysis**, the project aims to create an actionable and ethical tool that helps job seekers **optimize their resumes** while also understanding **what actually matters in hiring decisions** and addressing **potential biases in the hiring process.**
## Goals:
- Develop a resume analysis tool that evaluates how well an applicant aligns with specific job listings
- Visualizes which factors (e.g., experience, personality score, education level) most influence outcomes in your dataset
- Lets users simulate “what-if” scenarios (e.g., what happens if experience increases?)
- Analyze potential bias in hiring decisions
## Key Features and Innovations
- Resume Score & Factor Analysis
- Extract meaningful features from resumes and job descriptions using BERT embeddings.
- Provide a quantitative resume score based on key factors like skills match, experience, and education.
  - Offer percentile rankings based on hiring outcome data (e.g., "Your skill match is in the top 25% for this job").
## Hiring Outcome Analysis
- Analyze a dataset of real hiring outcomes to determine which resume factors influence success.
- Use SHAP values to see if gender or education unfairly influences hiring decisions
- Example insight: "Resumes with X certification have a 30% higher chance of getting an interview for software engineering roles."
## Data Collection Strategy
- Resumes: Scrape public resume datasets (e.g., Kaggle, Resume.io, OpenResume) and collect voluntary submissions from students/professionals.
- Job Descriptions: Scrape job postings from LinkedIn, Indeed, Glassdoor, and Handshake or use job board APIs.
- Hiring Outcomes:
  - Collect hiring data via surveys of students/professionals (e.g., job applications, interview outcomes, offers).
  - Explore collaborations with career services to access anonymized hiring data.
  - Utilize existing HR datasets or research papers on hiring trends.

## Expected Impact
Unlike existing AI resume tools that only provide text-based feedback, our tool will offer data-backed insights on hiring success factors. By analyzing real-world hiring outcomes, we can provide more transparent, actionable recommendations that go beyond generic AI-generated responses.
This approach makes our project uniquely valuable by focusing on data-driven insights rather than just text-based resume feedback.
  
## Data:
Resumes: Public datasets (e.g., Kaggle, Resume.io) and optional participant submissions

Job Descriptions: Scraped from LinkedIn, Glassdoor, Handshake, etc., or via job board APIs

Hiring Outcomes: Existing HR/recruitment datasets or anonymized records from career centers
## Data Model:
- BERT embedding to extract meaningful text features from resumes and job descriptions
- Logistic regression (job offer prediction to classify resumes as “likely to get an offer” vs. “unlikely)
## Data Insights & Visualizations

- Word Clouds: Highlight most frequently used skills and keywords across resume categories

- Category Distribution: Visual breakdown of resume categories (e.g., Data Scientist, HR, Developer)

- Market Expectations:

  - Compare experience requirements across job types

  - Identify top in-demand skills per role

- SHAP Summary Plots: Show which features most affect hiring predictions

- Dependence & Waterfall Plots: Explain individual predictions and feature interactions


## Modeling Pipeline: 

1. Preprocessing

  - Resume text consolidation into a single feature field

  - Cleaning and normalization of job descriptions and outcomes

2. Feature Extraction

  - TF-IDF for baseline model

  - BERT embeddings using sentence-transformers for semantic matching

3. Model Training

  - Baseline Logistic Regression with TF-IDF

  - Advanced model using BERT + Logistic Regression or Random Forest

  - SHAP integration for model interpretability

4. Evaluation Metrics

  - Precision, Recall, F1-Score, and Accuracy

  - Special focus on hired (positive) class performance

## Preliminary Results

- Baseline model using TF-IDF achieved high classification accuracy (~99%) across resume categories

- Initial classifier for hiring decision prediction achieved ~70% accuracy, but with low recall on the hired class, suggesting class imbalance and the need for deeper feature modeling

- SHAP analysis on ExperienceYears showed expected trends (e.g., more experience increased hire likelihood), but also prompted further investigation into less obvious patterns and biases


