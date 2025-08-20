# Used Libraries 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import TfidfVectorizer

# Importing Data 
raw_data = pd.read_csv("train.csv")

# Preparing the Data for cleaning
label_cols = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'] 
raw_data["bully"] = (raw_data[label_cols].max(axis=1) > 0).astype(int)
raw_data = raw_data[["comment_text", "bully"]]

# Data Cleaning
raw_data = raw_data.copy()
raw_data["clean_text"] = (
    raw_data["comment_text"]
    .str.lower()
    .str.replace("http", " URL ", regex=False)   
    .str.replace("www", " URL ", regex=False)
    .str.replace("@", " USER ", regex=False)    
    .str.replace(r"[^a-z\s\U0001F600-\U0001F64F]", "", regex=True)  
    .str.replace(r"\s+", " ", regex=True)   
    .str.replace(r"\d+", " NUM ", regex=True)
    .str.strip()                                
)

cleaned_data = raw_data[['clean_text', 'bully']].copy()

# Division into label and target
x =  cleaned_data['clean_text']
y = cleaned_data['bully']

# Splitting Into Training and Testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .2, random_state = 42, stratify = y)


# Vectorization On Text Strings
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
x_train_tfidf = vectorizer.fit_transform(x_train)
x_test_tfidf  = vectorizer.transform(x_test)
