# Used Libraries 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

# Train Logistic Regression
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(x_train_tfidf, y_train)

# Train SVM (Support Vector Machine)
svm_model = LinearSVC(random_state=42)
svm_model.fit(x_train_tfidf, y_train)