# Toxic Comment Detection using Machine Learning

## Project Overview
This project focuses on **training and evaluating machine learning models** to automatically detect *toxic or cyberbullying comments*.  
I applied **Logistic Regression** and **Support Vector Machine (SVM)** to classify comments.

## Motivation
Cyberbullying is a growing issue on online platforms.  
This project demonstrates how **machine learning can help identify bullying text** and create awareness online.

## Tech Stack
- Python  
- NumPy, Pandas (data handling)  
- Matplotlib, Seaborn (visualization)  
- Scikit-learn (Logistic Regression, SVM)  

## Dataset
- **Toxic Comment Classification Dataset**  
- For more details, see the dataset's README.

## Results
- **Logistic Regression:** Higher recall (catches more toxic cases)  
- **SVM:** Higher precision & accuracy (fewer false alarms)  

> Chose **Logistic Regression** as the final model because **recall is more important** in cyberbullying detection than overall accuracy.

## Workflow

### 1. Data Preprocessing
- Lowercased text  
- Removed extra punctuation, spaces, and special characters  
- Replaced emojis with word equivalents  
- Retained meaningful numbers  

### 2. Feature Engineering
- Applied **TF-IDF vectorization** to capture rare bullying words effectively  

### 3. Model Training & Prediction
- Trained **Logistic Regression** and **SVM** models  
- Stratified train-test split to handle class imbalance  

### 4. Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  

