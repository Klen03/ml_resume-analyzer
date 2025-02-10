# CS506 Project - Resume Analyzer

## Project description:
Resume Analyzer is a machine learning-based system that evaluates resumes, provides personalized feedback, and predicts the likelihood of a candidate receiving a job offer based on previous hiring patterns. Additionally in this project we also want to investigate whether there are biases in hiring decisions based on ethnicity, gender, disability, veteran status, and sexuality by analyzing historical hiring data.

By using **Natural Language Processing (NLP), machine learning models, and statistical analysis**, the project aims to create an actionable and ethical tool that helps job seekers **optimize their resumes** while also addressing **potential biases in the hiring process.**

## Goals:
- Develop a resume analysis tool that evaluates how well an applicant aligns with specific job listings
- Predict job offer likelihood
- Analyze potential bias in hiring decisions
  
## Data:
- Resumes from public resume library/ database (e.g., Kaggle, Resume.io, OpenResume)
  - Method: Scraping public resume datasets or collecting resumes from willing participants (e.g., students, professionals)
- Job descriptions from job websites (e.g. LinkedIn, Indeed, Glassdoor, Handshake)
  - Method: Scraping job descriptions or using job board APIs
- Dataset that includes hiring outcomes (e.g., research papers, HR datasets, or self-collected surveys)
  - Method: Survey students/professionals on their job applications and outcomes  

## Data Model:
- BERT embedding to extract meaningful text features from resumes and job descriptions
- Logistic regression job offer prediction to classify resumes as “likely to get an offer” vs. “unlikely)
## Data Visualization: 
- Radar chart  to visualize strengths and weaknesses of resumes based on key metrics such as skill match, experience, education, etc.
- Scatter plots to show feature importance vs. job offer probability
## Testing: 
- Unit test to verify correct feature extraction
- Dataset split, 20% for testing and 80% for training
- Use past records of resumes, job descriptions, and hiring outcomes to train data

