# Toxic Comment Detection using Machine Learning  

## Project Overview  
This project is focused on *training and Evaluating Machine Learning models* to automatically detect *toxic / cyberbullying comments*. I used Logistic Regression and SVM(Support Vector Machine) for it. 

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
## Results:

Logistic Regression → higher Recall (catches more toxic cases )

SVM → higher Precision & Accuracy (fewer false alarms )

I preferred Logistic Regression Results becuase *Recall is More important* - Catching maximum toxic cases matters more in Cyber Bullying than accuracy. 

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
    is it fine and according to my project it's github's readme file
