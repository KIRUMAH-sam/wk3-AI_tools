## AI Toolkit Project – Handwritten Digit Recognition & NLP Review Analyzer
**Objective:**  
> Build and deploy AI tools showcasing the power of machine learning and natural language processing using TensorFlow and spaCy.

---

## 📘 Project Overview
This project contains **two main AI applications**:
1. **Handwritten Digit Recognition using TensorFlow** – a Convolutional Neural Network (CNN) trained on the MNIST dataset to classify handwritten digits (0–9).  
2. **Amazon Review Analyzer using spaCy** – a Natural Language Processing (NLP) demo that identifies key entities (brands, products, etc.) and sentiment patterns in customer reviews.

These tools were later integrated into a **Streamlit App** for deployment and visualization.

---

## Features
### 1. Handwritten Digit Recognition (CNN)
- Dataset: [MNIST](https://yann.lecun.com/exdb/mnist/)
- Framework: TensorFlow/Keras
- Model: 3-layer Convolutional Neural Network
- Target Accuracy: **>95%**
- Outputs:
  - Model training accuracy & loss curves
  - Sample predictions with confidence levels
  - Confusion matrix visualization

### 2. NLP Review Analyzer (spaCy)
- Uses **spaCy’s `en_core_web_sm`** model for entity recognition
- Extracts and highlights:
  - Brands, products, and sentiments from reviews
  - Named entities in color-coded visualization using `displacy`
- Example input:
  ```text
  "I love the new Samsung Galaxy phone! The camera is stunning."

## Deployment
The model was intergrated into a streamlit app for deployment and the live link is provided here: https://kirumah-sam-wk3-ai-tools-app-7f9hkn.streamlit.app/

###LMS Article
The Article contains answers to the theoretical section of this assignment, showing in detail my understanding of the AI tools. It also analyzes the ethical optimization of the model
we created and gives in detail what is required and what is not.
