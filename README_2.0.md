\# CS506 Project - Hiring Intelligence Dashboard

Our project reimagines resume analysis by shifting focus from vague AI suggestions to data-driven insights based on real hiring outcomes. Rather than trying to predict job offers directly, we analyze which resume traits most strongly correlate with success—using actual recruitment data, SHAP interpretability, and behavioral scoring. Our tool empowers job seekers not just with feedback, but with explanations and comparisons, allowing them to simulate changes, view trait benchmarks against successful applicants, and identify potential bias or inequality in the hiring process. We aim to move beyond generative feedback and toward transparent, evidence-backed recommendations. This provides applicants with quantifiable and context-aware recommendations. 

\


\### MIDTERM REPORT PRESENTATION: <https://youtu.be/dAWN00tTHm4>

\### FINAL REPORT PRESENTATION: 

\


\## Project description:

\


By using \*\*Natural Language Processing (NLP), machine learning models, and statistical analysis\*\*, the project aims to create an actionable and ethical tool that helps job seekers \*\*optimize their resumes\*\* while also understanding \*\*what actually matters in hiring decisions\*\* and addressing \*\*potential biases in the hiring process.\*\*

**1, data selection and cleaning**

All the data are stored in csv form, and could be found under the dataset folder.

dataset/raw\_data:

‘job\_data.csv’: 

<https://www.kaggle.com/datasets/marcocavaco/scraped-job-descriptions>

**Contents:** Individual job descriptions and their assigned categories\
**Usage:** Generate BERT embeddings for each description and compare them to the user’s resume embedding to assess semantic alignment.

\


‘jobss.csv’:

<https://www.kaggle.com/datasets/thedevastator/predicting-job-titles-from-resumes/data>

**Contents:** Job titles, categories, and the corresponding lists of required skills\
**Usage:** Identify which high-frequency skills are missing from the user’s resume.

\


‘Recruitment\_data.csv’:

<https://www.kaggle.com/datasets/rabieelkharoua/predicting-hiring-decisions-in-recruitment-data>

**Contents:** Applicant features (e.g. education level, referral status) plus a binary hiring outcome

**Usage:** Train a LightGBM model and apply SHAP to determine which applicant attributes most strongly drive hiring decisions.

‘Resume\_data.csv’

<https://www.kaggle.com/datasets/saugataroyarghya/resume-dataset>

**Contents:** Structured applicant data—skill sets, educational institutions, timestamps, etc.—but no hiring outcomes\
**Usage:** Produce exploratory visualizations of applicant demographics and qualifications.

\


‘Resume.csv’

**Contents:** Plain-text resumes and their associated categories\
**Usage:** Extract top keyword lists and compute BERT embeddings to compare peer resumes with the user’s own.

\
\


dataset/processed\_data:

‘Cleaned\_job\_data.csv’: cleaned version of ‘job\_data.csv’

‘Cleaned\_recruitment\_data.csv’: cleaned version of ‘recruitment\_data.csv’

‘Cleaned\_updated\_resume\_data.csv’: cleaned version of ‘resume\_data.csv’

‘Encoded\_cleaned\_recruitment\_data.csv’:cleaner version of ‘recruitment\_data.csv’ (cleaners just means all categorical columns are encoded into numerical)

‘Jobss\_cleaned.csv’: cleaned version of ‘jobss.csv’

‘Plain\_resume.csv’: cleaned version of ‘resume.csv’

/keywords:

‘Cleaned\_jobdata\_keyword\_freq.csv’: stores the top 50 keywords of job description in each category’. Run all cells in “noteboooks/keyword\_extract/extract\_jd\_keywords.ipynb” to get this csv

‘Industry\_top\_skill\_keywords.csv’: stores the top 50 key skills in each category. Run all cells in “noteboooks/keyword\_extract/extract\_keywordOfSkills\_in\_jobss\_cleaned.ipynb” to get this csv

‘Plain\_resume\_keyword\_freq.csv’: stored the top 50 key skills of resumes in every category. Run all cells in “noteboooks/keyword\_extract/extract\_keyword\_plain\_resume.ipynb” to get this csv

/subsets\_by\_gender 

Every Files under this path will be explained in part 3, in “Subset creation and analysis Ivan.ipynb”

**2, statistical analysis and data visualization**

**_All the files that are addressed in this part can be found under the file called ‘notebooks’:_**

**File 1 - Directory: final\_visualization/encoded\_cleaned\_recrutment.ipynb:** 

**To get the following images, run each cell of the ipynb file sequentially.**

1. **Scatter Plot: SkillScore vs. InterviewScore by Hiring Decision:**

- _Purpose:_ To visually explore how skill and interview scores influence hiring decisions.

* _Explanation:_ Each point represents a candidate, with their SkillScore on the x-axis and InterviewScore on the y-axis. Circles represent candidates who were hired, while X’s represent those who were not. This plot reveals clusters and thresholds associated with success.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd9A6D9Ph-rAg03pdcRGZdS9noYVQv-UZlqlf85x0DeIsmIK91SkX1_g21EsYT6C28QmSb-lCj-0hRus7m8-HJUa3MqFnT6bjfZ2j2PkWl4m2FpUXh2qVMk6GRIkOZoOK8IY5vy?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Key Takeaways:_

  - Hired candidates cluster in the upper-right quadrant, where both skill and interview scores are high.

  - Very few candidates with low SkillScore are hired, regardless of their Interview Score.

  - There are a few edge cases where high-skill candidates were not hired, likely due to other factors (e.g. personality, fit, recruitment channel).

* _Implication for Analysis:_ This plot suggests that SkillScore and InterviewScore are strong indicators of hiring likelihood, especially when both are above \~70.

2. **Boxplot of PersonalityScore by EducationLevel:**

- _Purpose:_ To analyze how personality ratings differ by educational background.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcJl0bmS-Imoy-IWn0-dxOulN-Zbmj5GDEeh6ODb6WZp5KdCSaz3EiL50Cm_6e8EjdC8J79foGkGU10OuhnlIs-CjwNLMgTKHIgJb5viFzMuERka_z7T3DOd_lAcQIZnsB3jUt4?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Explanation:_ This box plot shows the distribution of PersonalityScore across EducationLevel groups (e.g. High School, Bachelor, Master, PhD). It includes medians, quartiles, and outliers, highlighting consistency and variability.

* _Key Takeaways:_

  - PhD and Master’s degree holders tend to have higher and more consistent personality scores.

  - Bachelor and HighSchool groups show wider variability and lower medians.

  - The presence of outliers indicates occasional strong candidates across all levels.

- _Implication for Analysis:_ This plot supports the hypothesis that higher education may correlate with stronger interpersonal traits, though variability within lower education levels suggests that strong personalities can emerge from all backgrounds.

\


3. **Bar Chart of Hiring Rate by RecruitmentStrategy and Education Level:**

- _Purpose:_ To evaluate the effectiveness of different recruitment strategies across education levels.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfLoQzuF13jG3fvOzBgISQBP6NOij6nn-DmCsYEyx6xWkFHgdnNLUni_GHDZIOJz49vGZNT0yUEujCe30BZqU421asw1gzZYfNgcty4MqfW4XJ-d14wu5GyJ8IjSr7_eN0C8FHUGw?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Explanation:_ This grouped bar chart shows the percentage of candidates hired for each RecruitmentStrategy (Referral, Online, Agency), with separate bars for each EducationLevel. It reveals how strategy and education intersect to influence hiring success.

* _Key Takeaways:_

  - Referral-based candidates consistently have the highest hiring rates across all education levels.

  - Online applications are moderately effective, while agency hired tend to have the lowest success rates.

  - The gap between strategies is most pronounced among Bachelor and Master degree holders.

- _Implication for Analysis:_ Referral programs yield higher success rates should be prioritized for sourcing candidates, especially for mid-to-senior roles.

4. **Parallel Coordinates Plot: Hired vs. Not Hired Profiles:**

- _Purpose:_ To compare multivariate candidate profiles between hired and not-hired groups.

* _Explanation:_ Each line represents a candidate’s normalized values across four metrics: InterviewScore, SkillScore, PersonalityScore, and ExperienceYears. Lines are color-coded by hiring outcome. This allows you to visually trace what makes a “typical” hired candidate different from a successful one.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc2mo8_3j_FK7FGTZGijLldRdFQGTr6tn8hTWBfK2kzIivIG5pYg_13Tp5WYjxzEJwpV0HVZFpoRUYi7ccDf65ZdV4naZX3mb8fsKBsC49_Jfu0yNAzVs_ZR5kwPiW9gPQi4ev_7A?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Key Takeaways:_

  - Hired candidates consistently score higher across all metrics, especially SkillScore and InterviewScore.

  - Differences in ExperienceYears and PersonalityScore are present but less stark. 

  - The visualization clearly separates groups, suggesting that a weighted combination of these metrics could effectively predict hiring outcomes.

* _Implication for Analysis:_ This confirms that successful candidates follow a multi-metric profile. A scoring algorithm or ML model can leverage these patterns for decision making or recommendations.

\
\


**File 2 - Directory: mid-term\_visualization/visualization.py:**

**To get the visualization, run this .py file, and the result will be under ‘datasets/visuals\_images’**

**Resume Keyword Frequency Analysis:**

As part of our data exploration, we conducted a keyword frequency analysis on the raw resume text. We used a custom keyword list to identify how often programming languages and machine learning (ML) concepts appeared across all candidates’ resumes. This analysis helped us understand the technical depth and focus areas in the applicant pool.

1. **Top Programming Languages (Keyword-Based):**

_What it shows:_ This bar chart displays the most frequently mentioned programming languages based on keyword presence in resume text.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXerbXVmUjEC83StFd0AwMofgELVoDde8XlpYaC-WR1ufBgIAeHhb6BlseJNqpG1cBAOpN2I6sHEcPoodvQ4iHfy8NhbNnGOiFwtnu51gd5RbWws9bQiBtN-JsMzkKe_-Xahxxw?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Method:_

  - We searched each resume (after cleaning) for mentions of common programming languages like “Python”, “Java”, “C++”, “SQL”, etc.

  - Mentions were case-intensive and counted even if they appeared as part of larger phrases.

* _Key Takeaways:_

  - Python dominates the candidate pool, followed by SQL, Java and JavaScript.

  - Languages like C++ and R appear less frequently, suggesting most candidates come from data-centric or full-stack backgrounds.

2. **Top Machine Learning Skills (Keyword-Based):**

_What it shows:_ This chart highlights the most common ML techniques and concepts mentioned across resumes. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXctrQLW0eh064iTeMzpa0RgAdvgOFOkw2kPoKzvGRvnDnQi0Rpir7d-ChuQmguSKz2q1P344LJdc_UoUTUiGNdRIADSNYmfc3Pn61sbtwTkQ8EPZCwPoaRcB0JP55j9Atq5jS99lQ?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Method:_

  - We compiled a targeted list of keywords such as “regression”, “SVM”, “random forest”, “topic modeling”, “neural network”, etc.

  - The code scanned each resume’s text and tallied keyword occurrences to find the most prevalent techniques.

- _Key Takeaways:_

  - Regression, clustering, and random forest are the most cited techniques.

  - Advanced topics like deep learning, topic modeling (LDA/NMF), and neural networks also appear frequently, reflecting a technically skilled applicant base.

3. **Why It Matters:**

This analysis was important for two reasons:

1. It helped validate the presence of high-value skills across resumes, which we later tied to hiring outcomes and recruitment strategies.

2. It informed the feature engineering process for our final model by surfacing keywords we could use to quantify domain expertise.

**File 3 - Directory: mid-term\_visualization/visualization\_jobss.py:**

**Job Market Landscape Analysis:**

This section summarizes our exploratory data analysis (EDA) of a cleaned job listings data. This visualizations help contextualize demand patterns in job roles, industries, experience requirements, and the specific sets requested by employers.

1. **Top 10 Most Common Job Roles:**

- _Purpose:_ Identify which job titles are most frequently offered in the dataset.

- _Insights:_ 

  - Shows which roles dominate the current hiring landscape.

  - Useful for aligning resume optimization with high-frequency opportunities.

- _Example:_ Roles like Software Developer, Data Analyst, and Project Manager appear at the top, indicating consistent market demand.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd3rQpAMs3tyHPDZdMlDnnB2uZJhO_a3cL6TiLgOuD9gqUW9oOoAVLhF-os07cG0_kI80mBRIouZP7Ke3LI3N6WAo8DqLs0zL_ph9vvnwwNa373S_l59mY3OBLgrFJE2CY3ACA0dQ?key=AydKl4-5KABXmLdy7Lo3PixK)

2. **Distribution of Minimum Experience Requirements:**

- _Purpose:_ Visualize how much prior experience is typically required for job listings.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfF5n2UCAAshSYXjDU5HB9ieEBej4M5wneRzZ2Dm-RYH1X3bKCI19DI5JO7unvllLcEgJwt19nfPh8Uu0W9_jQJ40L1zpKB0Mk9xVX2nFCdNkRPQftrddcMbXiw8bJ33EE3N68f?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Insights:_

  - Most roles require between 0-5 years of experience.

  - The histogram is skewed right, confirming that many roles are entry-to-mid level positions.

- _Use:_ Helps filter which resumes should be benchmarked against which roles during evaluation.

3. **Top 10 Industries with Most Job Openings:**

- _Purpose:_ Explore which industries are hiring most actively.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdQnHrbQfnF_0f49NrnUtw5932HI1KXFrc8etWuICzQ2Uy8cx1TAI0VJV2LrFgfDRrL6rNOjG-r0YUqFd9rVsdWSvpunQAQZs-235oE-S_vZhyXsl0x6JEkVPO2B9-KePreNQD2Fg?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Insights:_

  - Tech and IT services dominate, but finance, healthcare, and education also appear prominently.

  - This helps position a candidate’s experience toward industry-aligned roles.

4. **Top 15 Most Required Skills:**

- _Purpose_: Understand the technical and soft skills in highest demand.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf3UI1gl8_vTplgC6Q0Rv0_J_WJET9oCkjnfORu14YMpBvfoZ8bFgpMzt3wyq-dXXw45SwQcmNi6XHi1_BFc3aeLeUAXU5llcPW8YCioOH1Dzy7rtLCEfiIY-vVjCtoFTZYRS7N?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Insights:_

  - Skills like communication, python, SQL and problem-solving top the list.

  - Reflects both hard and soft skills crucial to employers.

- _Use:_ Useful for weighting skills in resume evaluation or for guiding candidates to fill in knowledge gaps.

5. **Experience Requirements by Role Category:**

- _Purpose:_ Compare experience thresholds across job categories:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfq8Vdf9E1YzWiA4qYXdwwa1mFJV14q2BH5aRyWScVhdo19SaXTPtRPFFw5ip1qLoxhLHyOmFM-oLhD07qAH_4pmVtqYxT5GseNhVua7cWOV3gnXGoQGNG0g6QNWPu9_uKtTfQO?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Insights:_

  - Roles in Engineering and IT demand higher experience.

  - Support or entry-level roles cluster around 0-2 years experience.

- _Use:_ Important for segmenting evaluation logic based on target role complexity.

\


6. **Top 10 Functional Areas:**

- _Purpose:_ Highlight the most common job functions (e.g., Engineering, Sales, Operations)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf0Usdzgn-5GZIMTnbApB6vS6SAWyaIBARwhic25sWiRhNNcUiSKwt-QRadUucYF7xM0UpSNgpD9qQVUe3u5tUm-da1jyW4magKWidO2ZAz5qTCli2b7vXB5ALuFMLES97V4mha?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Insights:_ 

  - Emphasizes demand for tech-centric roles (Engineering, Data) as well as business units like Sales and HR.

  - Use for candidates planning to pivot to high-opportunity domains.

7. **Number of Skills vs. Experience Level:**

- _Purpose:_ Analyze how the number of required skills varies by years of experience.

****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXek5QRGeHr9vcSXZRj2kRN4Ag0yT1Tm041i1KThT0_ehypc43x8GEV6dZtVNFZs08TFNIAOr6xm74iBW5i1q67EJEJFCwnlj80B2W4Qo8h77p2QpDEQ57LagpQEXXwUuup-ExrX9w?key=AydKl4-5KABXmLdy7Lo3PixK)****

- _Insights:_

  - Entry-level jobs (0-2 years) require fewer skills (\~5-6 on average).

  - Senior roles (8+ years) list up to 10-12 required skills.

  - Confirms that complexity scales with experience.

8. **Top 3 Skills Required for Top 10 Job Roles:**

- _Purpose:_ Break down skill demand by specific job titles.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfeyHeLx8GoskLOzNcG-ohCmaqbHbzEr-vG81Da8Xj4Inp6h8r6rSFPP8lvP2-WO9r7UI52yx0b1vX7qqN2fNpcs_D9CXjA0OJhdsoWjBCawVEreN0un0YSdEGCoB5hZbsXLlrTpQ?key=AydKl4-5KABXmLdy7Lo3PixK)

- _Insights:_

  - For example, Python, SQL and Data Visualization dominate Data Analyst roles.

  - Each job title has a distinct top-3 skills “signature”.

- _Use:_ Essential for resume-tailoring: match candidate skills to the exact traits employers expect per role.

**Summary**

_This analysis helped us:_

- Contextualize our resume evaluation dataset against real market demand.

- Guide feature selection (e.g., which skills to encode).

- Understand how experience, skills and roles interconnect, improving control-group logic for evaluating hiring fairness.

\


**File 4, 5, 6 - Directory: ****keyword\_extract/extract\_jd\_keywords.ipynb &**

******keyword\_extract/extract\_keyword\_plain\_resume.ipynb& ****keyword\_extract/extract\_keywordOfSkills\_in\_jobss\_cleaned.ipynb**

In these three files, I:

**A.** From cleaned\_job\_data.csv, extracted the top 50 keywords and their counts for each category’s job descriptions, and saved the result to

‘datasets/processed\_data/keywords/cleaned\_jobdata\_keyword\_freq.csv’

**B.** From plain\_resume.csv, extracted the top 50 keywords and their counts for each category’s resumes, and saved the result to

‘datasets/processed\_data/keywords/plain\_resume\_keyword\_freq.csv’

**C.** From jobss\_cleaned.csv, extracted the top 50 required skills and their counts for each category, and saved the result to

‘datasets/processed\_data/keywords/plain\_resume\_keyword\_freq.csv’

All the keywords will be crucial references when we are analyzing user’s resume in 

‘notebooks/user\_resume\_analyze.ipynb’. Detailed Explanation can be found in part 4.

**—-How to run:**

To get all the keywords csv, run every cell sequentially. 

**File 7- Directory: noteboooks/mid-term-visualization/visualize\_resume\_keyword.ipynb**

I applied word‐cloud visualizations to the file datasets/processed\_data/keywords/plain\_resume\_keyword\_freq.csv, 

generated a word cloud of the top keywords for each category, and saved all the images to 

datasets/visuals\_images/wordcloud\_resume\_keyword. The result looks like this:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUbugKjncZGjt8wX2gXkTWs4Cn1ybM5HEQLBgjzc2ukLe75zQk8LtmZUyfL7j9xna2pVJucQe5pjHbzBeCGs3kg7Y6z15qEuYA8ILoCjxDZdpKP3Z-wea3wcIMVvA4EWe7OCg_?key=AydKl4-5KABXmLdy7Lo3PixK)

**—-How to run:**

To get all the word-cloud visualization images, run every cell sequentially.  

\


********

**3, data modeling and SHAP analysis**

All the following files are under the file of notebooks:

‘SHAP.py’: this is the groundwork of the following two files, so no need to run this file

In ‘**SHAP\_revised\_by\_zetian\_0428.ipynb’**:

Reads the encoded recruitment data from “datasets/processed\_data/encoded\_cleaned\_recruitment\_data.csv”, which contains columns: (ExperienceYears, InterviewScore, SkillScore, PersonalityScore, Gender\_encoded, EducationLevel\_encoded, RecruitmentStrategy\_encoded) and target (HiringDecision).

Gender\_encoded: 1 = male, 0 = female\
RecruitmentStrategy\_encoded: 2 = referral, 1 = online, 0 = agency\
EducationLevel\_encoded: 0 = High School, 1 = Bachelor, 2 = Master, 3 = PhD\
\
Trains a LightGBM classifier Prints a classification report (precision, recall, F1)\
Plots feature importance by gain via lgb.plot\_importance

Uses SHAP to compute and plot a summary of how each feature influences predictions:****![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfYG-ODmLVy0NKd1GZWXvROSdfW_pb8xqqrSNbyVYuTRZ2OPfG-OfMm9doXMEJ9n103vB6Nc_pq_sUqmYU9b4UKShbjTwLaqzX-b0r_iw_VkinhhHnsZQBulgqJhwPdTKrvcjl9Ew?key=AydKl4-5KABXmLdy7Lo3PixK)****

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeeRLWITye78Hh-SfVBR3vGgvyJhNJztB5ByzFztN5Q-A6TM5fa0EpP5WJukKHLpZ67lIEhZNDkWREfR-p5TPCqb70pyQOWRZ2MeWiHAEHfO2rCfqZH4JTbHPvDHtgwQvbpijoLqg?key=AydKl4-5KABXmLdy7Lo3PixK)

From both analyses, it’s clear that **RecruitmentStrategy** is the most important factor (i.e. whether an applicant applies online, through an agency, or via referral). If someone is referred (i.e. has a company referral letter), their success rate increases dramatically. **Personality**, **skill**, and **interview** scores are far less important than referrals. Interestingly, **education level** is not as influential as **experience years** or any of the factors above. Finally, **gender** has almost no impact on hiring outcomes, reflecting that the modern labor market does not exhibit severe bias.

Building on this, the next notebook will explore subsets of the data, for example:

1. “For candidates with referrals, which factors are most important?”

2. “For male versus female applicants, which factors differ most in their impact on outcomes?”

\


**“Subset creation and analysis Ivan.ipynb”** : this is the file where we create subsets of the dataset and perform SHAP analysis on each of the subsets

File relative path: noteboooks/subset creation and analysis Ivan.ipynb

We realize that in “recruirtment\_data.csv”, there are many interesting columns as listed above. As we want to offer suggestions to certain demographics of people, we decided to create subsets based on genders and see what are the most important factors for male or female applicants and will boost the possibility to get them hired.

Here’s the detailed explanation of the codes:

We first save the cleaned version of the encoded recruitment data. And then we set the path to save the new subsets and create the subsets. As we discovered from the “SHAP\_revised\_by\_zetian\_0428.ipynb” that females and males have different influences on the final model output, for the first set of subsets we decided to separate male applicants from female applicants. We iterate through each unique gender in the cleaned data to get the features and save the files. Then we train and apply the LGBM in the same manner as we did to the whole dataset but this time on the subsets.

For females, we first read the female subset file and make sure that we don’t include the gender-related column to avoid extraction. Then we split the train and test set before performing the LGBM model.

Then we plot the graphs:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf-PLHpIlpovYmGF_bvBA3CNBHMr6aEfT0lxz7Dpq1qwpOkJe_GISB4sGf5oh7Dit1mcRcqkDHaGWPZSUH85O9dSSFrBMLPDtALTEjIJKaPisq9ULCI0yKo4X9zr9zJA_wvUQ82?key=AydKl4-5KABXmLdy7Lo3PixK)

We can see from the graph that recruitment strategy is the most important factor for females, way more important than the other factors. And education level is the least important factor. 

Then we calculate the SHAP values and plotted it:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf-Dlc1ESx62apCngpLfPGjYNu2LtMhVF6t4utDqLm_ejJQFtmRcuGGYgY3IObRQz_7vY7Uzkc_08Kjww0ujJedgMI7es897gdiWR7o6baq6Y4d5y5FeJkzhPupfJJan2_-DklYGQ?key=AydKl4-5KABXmLdy7Lo3PixK)

For all the features, it is generally that the higher the feature values, the more positive impact they have on the model output, which does make sense because the features all represent something positive. It would benefit the companies to hire people with a higher positive score.

But the three recruitment strategies are “online”, “referral”, and “agency”, which do not necessarily have a “positive” or “negative” inference.

As the recruitment method is also the most important deciding factor to the hiring outcome according to the LGBM analysis, we think it is meaningful to further analyze the subsets of each recruitment strategy under each subset of genders. So we first applied this to the female subset.

There are three different recruitment strategies: referral(encoded with 2), online(encoded with 1), and agency(encoded with 0). We basically repeated the same process as before, just three times for three recruitment strategies this time(we are using the female subset as the base). 

Here is the output of the female who do referral:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcysCnuqj6y67XzpMlyTX-5Dk5NkC8sqM0lJHiCy9d0V6lBXit3zd1zQ2zWpQoOo98vIVTVaUm6D4PoHAikBnlsWZG4KJX_g8NA_Cu43ntGJUqOQoXZ9muiGdgwtxzl6ANFK6bUgA?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeOHXKFjrF8IXLpExaFfPOculnj81eaWPSILWY-Gh1L8F_IPyi7K8w2T1EjI0EWrNRMG40Tqb3zfJVCQfm6VWxlrrCSHrtX9pUhvqH0fsHJ6ikA1sGr-18z-jPZ9rjbxR7NLuD3?key=AydKl4-5KABXmLdy7Lo3PixK)

For this demographic, the rank of feature importance is: SkillScore, ExperienceYears, PersonalityScore, InterviewScore, and EducationLevel. 

For these features, it is generally that the impact is positively correlated with the feature value. However, sometimes a high interview score might lead to negative influences on the final outcome.

\
\
\
\
\
\
\
\
\
\
\
\
\


Here is the output of the female who do online:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdRzuSn2n_-rDmMw_3U42_0KRWo6bX5DkiCF0tOO_GBnhBMOyecw3GOh5FZQmBZPQ9RCUo_5eoP0cA_3fzqpvaI5aA1Yti0zEKpTaSc2w-CDLWZa9tFCqtfi9HHPJT4m6TFRlvM?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfsK6Vj2FRbFgEe8aib06p98wu8cFBHQW_NYTKEPB8CGjX4AOts-BldIzN8RIYwdSqPSy497yTwbCmgNglPfgJuQoVYvDaY3zHtDIEEEiBX7Tr9OEBfiBwN8kWKU_bm5drW7EBV?key=AydKl4-5KABXmLdy7Lo3PixK)

For this demographic, the rank of feature importance is: SkillScore, InterviewScore, PersonalityScore, EducationLevel, and ExperienceYears.

For the females who do online, high interview score, high skillscore, and longer experience years might harm the hiring outcome. But a good education level would almost guarantee a positive influence on the outcome.

We think it also makes sense because the employers might not trust the performance of the applicants during interviews as much since it is held online. However, education level is something that pre-existed and cannot easily fake.

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\


Here is the output of the female who do agency:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfRUFehZn3fY3x_m-zByqnZdrOAdKebN3bT0josgCUeETJEyBMlgQWGOIyX6HtyCpq1Jef_3v8U7ZZ7Z9t3hGeDmLeXT0ISXO2pQPXxCOkQoh7WQSqYRw_1690miU9T2zyoSizO7A?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeOjJacvJrQZBO_cYlbAOUMUE_9E-cEtYFt2MtGEswWU4DVZadzYg19Ha9MhHRhyWSUbkCHxb1FAcnT6yGZIM5JwqUOQfY0tEC7nSe2Q6mFNCaeYTt90SVxv1wBB-uo47HL6l_ZHw?key=AydKl4-5KABXmLdy7Lo3PixK)

For this demographic, the rank of feature importance is: PersonalityScore, ExperienceYears, SkillScore, EducationLevel, InterviewScore, and ExperienceYears.

For the females who do online, it is true that the higher the scores are, the more positive the influences they have on the outcome are. It matches the common sense.

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\


Then we conducted the same set of operations on the male subset:

Here is the output for the male group in general:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXen94D1xzr3qbM34_8BCOEyvlIaEipaOzzahSLEP23ooNxQLU8aDBPfPQShd-BGSdokf5JN0P3SofT5l6O8xJ3cCKdTS0U_Jqagfl_hsPY5BcxZ7DL-JH1obik0kdn4SNHWjDu1aA?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXewJ1qBWm16kVrN_y7d2ol0lzESx0FNxiXCZUKDdoCokFWJg66dzzg_z2FBmZqY3xBp5VoiE1qF-2L7TruQFmxOo_AFwU-IF4WiWr0q_JXYyulV9_9dpcR-rbbMIHpaeXFuqjt-pA?key=AydKl4-5KABXmLdy7Lo3PixK)

The two graphs match really well. In both of the graphs, the recruitment strategy is the most important factor. A high value of the encoded strategy (red) pushes predictions strongly positive, and a low value (blue) pushes strongly negative. The rank here is recruitment strategy, SkillScore, InterviewScore, ExperienceYears, and EducationLevel. PersonalityScore is the least impactful for males because its SHAP values cluster more tightly around zero, indicating it barely moves the prediction.

\


Then within the male demographic, we further subgrouped it according to the recruitment strategies. Here are our discoveries:

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\


For males who do referrals:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfuZUhIFHy4xRFH4w3xBQnYgZKy9y6rZ-yF-eKObOO1hitt5DEeWXrfNjwd8zYvIPfOa30i8gZa3ACb6wvPAXkHzXeUZIGeCtW0VsqzmlkeqRlJJ-UKPJX0j9oWVxeavKJSsJddsQ?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc66BfPOstR8cxj0f8dXuFJijVFkDV_nzf9MDo7lJrWgX-9_WgeJkPBKjsukwGzQHErrcrE_QZzkAy91cJO86J22NyF0wzQBhalHy3gDFU70_33gEe_s9n3IDyWM_hChJbnuYUy?key=AydKl4-5KABXmLdy7Lo3PixK)

According to LGBM, the importance rank is SkillScore, ExperienceYears, PersonalityScore,  InterviewScore, and EducationLevel\_encoded. And the SHAP summary chart also looks conventional. InterviewScore and PersonalityScore both have some noises, but in general the SHAP values and the feature values are positively correlated.

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\


For males who do onlines:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXezOXs4j_5a_m46kBXW7c6dXuxEehff2vZPs0XRvwqB3F-D-hr8cIRBbCd4hQX_14bfO-OCdJzumd1emMEpyNJFirijjM012Kb9EsQx5vbUY173zypkhulbm5fQJ8WMYtevXBbeKQ?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeXrJQE7-eMYiZCuQTWgS7W9Nk8Vbr4P9MAPGeGqMwclaQxU9gLkYNilPS1x6jF6dRI85aZiT8ipEB8rXyA_QnWuePOgQkanPwUBoins111jg0m2YKgHOk7XRJ8rVKl3xBjnioXTw?key=AydKl4-5KABXmLdy7Lo3PixK)

According to LGBM’s gain for the “Male – online” group, the features rank as PersonalityScore ,InterviewScore, SkillScore, EducationLevel\_encoded, and ExperienceYears  

In the SHAP summary plot ExperienceYears has the largest mean SHAP value since high years push positive more and  low years push negative more. As PersonalityScore’s dots are close to zero, it is the weakest mover. So among male applicants who choose to do interviews online, experience years are way more important than personalities.

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\


For males who do agencies:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeIX1O_Mc0kbK144YhSUNd9UTKG4hHWMD-e8Ixc9wN-1DplFNqIrPutCEj_abwMel1EqkBhXy6jt1GrJsTTdVKlGIKDgc6pI-lsbK9kQa2Cu2inVgmmkbA-xn_4eDiPj9a42GVE?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdGHDnSmfHX3oLvqw-ZWT9XRKBT_D2rCtKFzPK2gBhwBTR-s-6zMM-nl3Q9i4gfbMEEgxyMBzWmg5Z3ZS-XEPwcBiTX4cTNu6SAKC0hdEAECCttXxmUIwJKHd9pBlnQTgeMUy-Xdg?key=AydKl4-5KABXmLdy7Lo3PixK)

From the LBGM plot, the rank is InterviewScore, EducationLevel, SkillScore, ExperienceYears, and PersonalityScore. Although InterviewScore dominates the LGBM, ExperienceYears actually moves predictions the most on average. PersonalityScore barely budges the model either way (its dots hug the vertical zero line). So it is safe to say that for male applicants who do agency, the experience year is the key factor that influences the hiring outcomes.

\
\


Then, to make the visualization clearer, we plotted the male outcome and the female outcome together side by side.

Here is the visualization:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdKx0LOajqt561CtjK43o1pMzbDM5brMw5AsszjU42ntUnJ3unSqZkEtlWXLuyYfzL1ZH5IUFt7622ugIpJ67PEdcxQV4hcF8kNLApQ4deZityOqbEhJGumz5w4PyDlDjiAwo3Wrg?key=AydKl4-5KABXmLdy7Lo3PixK)

In this way, it is clearer that it is very close, but male applicants have an advantage over female ones.

\
\


Finally, we look at the recruitment data as a whole in general and subgroup them based on the recruitment strategies in the same manner as before.

\
\
\


For those who use referrals:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdb4L0SdBrqH7lbWjUUU-ISplFtW3FlwYPc7HTCZS91qMsom_smbLYIN-a6H5VIX79ryyqOdrvzd_5SajSvW8bsCoQEMX5vIBIDErf0JuKKwxLXde-zNpepviKfHm-lgFLLCsEI?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeer0jYg7hrdC-V5I-WS_1xnpwh3VU6fX2IxIiql-pXIi9izNkAw-Blhu1EYhFxGvo8TEW30Rs5G3jmXc-FadyJ7rJ9uQKEGZ5QBP5zajLP6nA0wrH51Cq5nQg_lU-GENuUnUEIzA?key=AydKl4-5KABXmLdy7Lo3PixK)

Both the LBGM and the SHAP summary show that SkillScore is by far the strongest predictor for referrals, with PersonalityScore and InterviewScore next in the gain ranking.

However, SHAP shows the true impact order as SkillScore, InterviewScore, EducationLevel\_encoded, PersonalityScore, and ExperienceYears. 

In contrast, gender doesn’t seem to influence the hiring decision when every applicant is under referral.

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\


For those who do online:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdAB6Iyf03I8aN9JjBidwJHNR5GzO4tmlAbrLEerL4RMzpvj1RBG07PhIoer-CwVmDV4Cb8yDTRGR0mDCkG0EwBSbEp2DMxNwLoLDNOLFHjciwUP_RVj40d-3jJEGsfTay6DQtQsg?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeBV3uZbQ728qoPoJ3HDmDyjoynULgRKCJsbwDAqJRVdVSd7_fUkMm2KQf3JsaaqdEwpIAbpoKjH4DNxv3dsd-HQ33UduDuF5a0RyqnIqjodm2BAc-MH3v9y8c25_mRyN9N7r2nyw?key=AydKl4-5KABXmLdy7Lo3PixK)

Both the LGBM and the SHAP summary for the online subset agree that SkillScore and InterviewScore dominate the tree splits, followed by PersonalityScore, EducationLevel\_encoded, ExperienceYears, and finally Gender\_encoded. 

However, SHAP reveals the true average contribution order is InterviewScore, PersonalityScore, EducationLevel\_encoded, SkillScore, ExperienceYears, and Gender\_encoded, with higher feature values (red) pushing predictions up and lower (blue) pushing them down. A higher interview score does not guarantee that the hiring outcome would be good, which is interesting.

Same as before, gender doesn’t influence much here.

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\


For those who do agency:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdQDpv2xY7imvP-iz0HSx4d3Pc4OKEfVVqn9yfugFKO8hAb2pbKpNsKaEwxRhZKftFz43la85mF19huNUIcmAlOJc56p33hDOSJ-mtisRIShg2sM1XBUq9RRXp89l7lQjOieVb6Hw?key=AydKl4-5KABXmLdy7Lo3PixK)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcbKFENUgV4x18z37-g6lQtUnkIT_K9QUV3DO4HbNgFH_QmQ0s5s4QLdGrH4ezcjwK7adp-olj64QGiFSD1-KNjLP2KTLpVKnpP0CYWeWtiRHQnsoNem3W5vKXsA3vsWERpb4h-9Q?key=AydKl4-5KABXmLdy7Lo3PixK)

Both the LGBM and the SHAP summary for the agency subset agree that PersonalityScore and InterviewScore dominate the tree splits, followed by EducationLevel\_encoded, SkillScore, ExperienceYears, and Gender\_encoded. 

However, SHAP reveals the true average contribution order is InterviewScore, PersonalityScore, SkillScore, EducationLevel\_encoded, ExperienceYears, and finally Gender\_encoded, with higher feature values (red) pushing the prediction up and lower (blue) pushing it down. 

Again, gender doesn’t have a big influence on the result.

\


**4, application - user resume analysis**

This part  contains a single notebook:

‘notebooks/user\_resume\_analyze.ipynb’. 

It automates a two-fold evaluation of your resume—semantic alignment and keyword coverage—against industry data. 

1\. Category Matching 

• Prompts you to enter your desired role (e.g. “Software Engineer”, “Data Scientist”, “UX Designer”). 

• Uses a BERT-based encoder to find the closest match among three system datasets: job descriptions, peer resumes, and skill requirements.

 2. Resume Ingestion 

• Reads your resume.txt from datasets/user\_resume/. 

• Tokenizes and embeds your full text for downstream analysis. 

3\. Semantic Similarity Scoring 

• Aggregates all job descriptions in the matched category and computes a cosine similarity score between this combined text embedding and your resume embedding. 

• Repeats the process for the collection of peer resumes to gauge how your profile aligns with industry standards. 

4\. Keyword Gap Analysis 

• Loads pre-computed top keywords (with frequencies) from: 

datasets/processed\_data/keywords/cleaned\_jobdata\_keyword\_freq.csv 

datasets/processed\_data/keywords/plain\_resume\_keyword\_freq.csv 

datasets/processed\_data/keywords/industry\_top\_skill\_keywords.csv

 • Parses each list and identifies missing high-frequency terms in your resume by applying substring checks and an embedding-based similarity threshold. 

• Highlights “key keywords” that are absent across multiple categories as priority areas to strengthen. 

5\. Report Generation 

• Prints concise similarity scores for both job descriptions and peer resumes. 

• Lists missing keywords per category alongside their frequencies.

 • Offers targeted recommendations on which skills or terms to consider adding. 

\


How to run: 

1\. Place your resume.txt in datasets/user\_resume/ and update its path in cell 

2\. Run all cells except the last one. 

3\. Execute the final cell and enter your category when prompted to see the full analysis.a
