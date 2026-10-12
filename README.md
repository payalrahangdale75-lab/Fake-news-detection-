# Fake News Detection using NLP

## Overview

This project focuses on detecting whether a news article is **Fake** or **True** using Natural Language Processing (NLP) and Machine Learning. The model was trained on more than **44,000 news articles** after applying text preprocessing techniques and TF-IDF vectorization.

Two machine learning models were trained and compared:

* Logistic Regression
* Passive Aggressive Classifier

The Passive Aggressive Classifier achieved the best performance with an accuracy of **99.64%**.

---

## Dataset

The project uses two datasets:

* **Fake.csv**
* **True.csv**

Both datasets were merged into a single dataset and duplicate records were removed before training.

---

## Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Text Preprocessing
5. TF-IDF Feature Extraction
6. Model Training
7. Model Evaluation
8. Pipeline Creation
9. Model Serialization using Pickle
10. Streamlit Application

---

## Text Preprocessing

The following preprocessing steps were applied:

* Converted text to lowercase
* Removed punctuation and special characters
* Removed stopwords
* Applied Porter Stemming

---

## Exploratory Data Analysis

The following visualizations were created:

* Fake vs True News Distribution
* Subject Distribution
* News Length Distribution
* Confusion Matrix
* Model Accuracy Comparison

---

## Models Used

| Model                         | Accuracy |
| ----------------------------- | -------: |
| Logistic Regression           |   98.94% |
| Passive Aggressive Classifier |   99.64% |

The Passive Aggressive Classifier was selected as the final model because it achieved the highest accuracy.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* NLTK
* Scikit-learn
* Streamlit
* Pickle

---

## Results

* Logistic Regression Accuracy: **98.94%**
* Passive Aggressive Classifier Accuracy: **99.64%**
* 85% accuracy on 40 manually tested recent news articles.

The trained model correctly classifies most news articles when provided with sufficient textual context.

---

## Live Demo

🔗 **Streamlit App:**  
https://fake-news-detection-3m6c6ekdj3m5vb2vbm94jv.streamlit.app/

---

## Limitations

- The model was trained on a specific fake news dataset, so performance may decrease on recent or unseen news articles.
- It performs best when given complete news articles rather than short headlines or single sentences.
- The model relies on TF-IDF features, which capture word frequency but do not fully understand the context or meaning of the text.
- Predictions may be affected by changes in writing style, vocabulary, or news topics over time.

---

## Future Improvements

* Flask-based web application
* Improved UI
* Deep learning models (LSTM/BERT)
* Deployment on cloud platforms

---

## Additional Validation

The trained model was manually tested on 40 recent news articles that were not part of the training dataset. It achieved approximately **85% accuracy** during this manual evaluation, indicating good performance on unseen news while also highlighting the limitations of TF-IDF-based models.

---

## Author

**Kunal Turkar**

B.Tech (Information Technology)

Interested in Machine Learning, Data Science, and Artificial Intelligence.
