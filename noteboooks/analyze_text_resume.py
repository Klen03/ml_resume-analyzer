import pandas as pd
from keybert import KeyBERT

df = pd.read_csv("datasets/processed_data/plain_resume.csv")

# 按 Category 分组，合并每个title的 Resume 文本
grouped_df = df.groupby("Category")["Resume"].apply(lambda texts: " ".join(texts)).reset_index()

grouped_df.to_csv("plain_resume_groupByTitle_beforeEmbed.csv")

kw_model = KeyBERT()

def extract_keywords(text):
    # keyphrase_ngram_range=(1, 2) 表示提取1到2词的短语，可以根据需要调整
    return kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english')

# 为每个类别提取关键词
grouped_df["keywords"] = grouped_df["Resume"].apply(extract_keywords)

print("每个岗位的关键词：")
grouped_df[["Category", "keywords"]].to_csv("plain_resume_groupByTitle_keyword_and_score.csv")
print(grouped_df[["Category", "keywords"]])
