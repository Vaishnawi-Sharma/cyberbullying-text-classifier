# Toxic Comment Detection using Machine Learning  

## Project Overview  
This project is focused on building a *Machine Learning model* to automatically detect *toxic / cyberbullying comments*.  

##  Why?  
Cyberbullying is a growing issue on online platforms. With the help of *Machine Learning*, this project demonstrates how technology can assist in identifying bullying text and creating awareness.  

---

##  Tech Stack  
- *Languages & Libraries*  
  - Python 
  - NumPy, Pandas (data handling)  
  - Matplotlib (basic plots)  
  - Scikit-learn (ML models: Logistic Regression, SVM)  
  - Seaborn
    
##  Dataset  
- Dataset: Toxic Comment Classification Dataset (For more info visit the data readme.md)  

---

##  Workflow  

1. *Data Preprocessing*  
   - Lowercasing text  
   - Removing extra punctuation & spaces & Special Characters 
   - Handling emojis → replaced with word equivalents 
   - Keeping meaningful numbers

2. *Feature Engineering*  
   - *TF-IDF Vectorization* (instead of Bag-of-Words, to capture rare bullying words with higher importance).  

3. *Model Training*  
   - Logistic Regression  
   - Support Vector Machine (SVM)  
   - Train-Test Split (stratified, to handle imbalance)  

4. *Evaluation Metrics*  
   - Accuracy  
   - Precision  
   - Recall  
   - F1-score  

