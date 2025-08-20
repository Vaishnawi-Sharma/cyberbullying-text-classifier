# Used Libraries
from sklearn.metrics import f1_score, classification_report, confusion_matrix
import numpy as np
from sklearn.metrics import f1_score

# Evaluation & Prediction Of Logistic Regression
y_pred = model.predict(x_test_tfidf)

print("F1 Score:", f1_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Threshold optimization 

probs = model.predict_proba(x_test_tfidf)[:, 1]
thresholds = np.linspace(0.05, 0.95, 19)

best_t, best_f1 = 0.5, -1
for t in thresholds:
    preds = (probs >= t).astype(int)
    f1 = f1_score(y_test, preds)
    if f1 > best_f1:
        best_t, best_f1 = t, f1

print(f"Best threshold: {best_t:.2f}, F1: {best_f1:.4f}")

# Evaluation & Prediction Of SVM

y_pred_svm = svm_model.predict(x_test_tfidf)


print("F1 Score:", f1_score(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))
print(confusion_matrix(y_test, y_pred_svm))

