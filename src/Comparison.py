# Comparison of Logistic Regression & SVM

# Used Libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, f1_score
import numpy as np

# For Comparision Matrix

# Logistic Regression predictions
y_pred_lr = model.predict(x_test_tfidf)   
cm_lr = confusion_matrix(y_test, y_pred_lr)
f1_lr = f1_score(y_test, y_pred_lr)

# SVM predictions
y_pred_svm = svm_model.predict(x_test_tfidf)  
cm_svm = confusion_matrix(y_test, y_pred_svm)
f1_svm = f1_score(y_test, y_pred_svm)

# Ploting confusion matrices side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.heatmap(cm_lr, annot=True, fmt="d", cmap="Blues", ax=axes[0])
axes[0].set_title(f"Logistic Regression\nF1 = {f1_lr:.3f}")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Actual")

sns.heatmap(cm_svm, annot=True, fmt="d", cmap="Greens", ax=axes[1])
axes[1].set_title(f"SVM\nF1 = {f1_svm:.3f}")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")

plt.tight_layout()
plt.show()

# For Bar Chart
models = ['Logistic Regression', 'SVM']

# Metrics for each model
precision = [0.588, 0.871]  # LR and SVM
recall = [0.854, 0.676]
f1 = [0.696, 0.761]

# X-axis positions
x = np.arange(len(models))
width = 0.25  # width of the bars

# bar chart
plt.figure(figsize=(8,5))
plt.bar(x - width, precision, width, label='Precision', color='skyblue')
plt.bar(x, recall, width, label='Recall', color='lightgreen')
plt.bar(x + width, f1, width, label='F1-score', color='salmon')


plt.ylabel('Score')
plt.title('Model Comparison: Precision, Recall, F1-score')
plt.xticks(x, models)
plt.ylim(0, 1)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()


# Saving Results into CSV

df_results = pd.DataFrame({
    'Text':  x_test,    
    'Actual': y_test,         
    'Predicted': y_pred      
})

# Save to CSV 
df_results.to_csv('logistic_predictions.csv', index=False)