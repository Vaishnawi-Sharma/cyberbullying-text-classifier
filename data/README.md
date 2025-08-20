# Dataset Information

This project uses the **Jigsaw Cyberbullying Dataset** from Kaggle.

- **Source:** [Kaggle – jigsaw-toxic-comment-classification-challenge](https://www.kaggle.com/datasets/julian3833/jigsaw-toxic-comment-classification-challenge)
- **File used in this project:** `train.csv`  
  - The dataset was split into 80% training and 20% evaluation.  
  - The Kaggle `test.csv` file was not used (labels are not provided).
  
- **Size:** ~160,000 social media comments
  
## Dataset Columns

- `comment_text` → the actual social media comment (text input).  
- Toxicity labels (binary: 0 = not present, 1 = present):  
  - `toxic`  
  - `severe_toxic`  
  - `obscene`  
  - `threat`  
  - `insult`  
  - `identity_hate`  

Each comment can have **multiple labels** (e.g., a comment can be both `toxic` and `obscene`).  


⚠️ The full dataset is too large to be stored in this repository.  
To run the project:
1. Download the dataset from Kaggle.

### Sample Data
A smaller subset of the dataset (`sample_data.csv`) with 350 rows is included in this repo for demonstration purposes.






