# 📄 AI-Powered Resume Screening System (NLP + DSA)

##  Project Overview
This project implements an **AI-powered resume screening system** that automatically evaluates and ranks resumes based on their relevance to a given job description. It leverages **Natural Language Processing (NLP)** and **Data Structures & Algorithms (DSA)** to provide an efficient, accurate, and scalable solution for resume shortlisting.

The system was trained and evaluated using a **Kaggle resume dataset** and achieved an **accuracy of 96%**, making it suitable for real-world recruitment scenarios.

---

## Methodology

### NLP Algorithm Used
- **TF-IDF (Term Frequency–Inverse Document Frequency)**
- Converts resumes and job descriptions into numerical feature vectors
- Captures the importance of keywords across documents

###  Similarity Measure
- **Cosine Similarity**
- Measures how closely each resume matches the job description

---

##  Data Structures & Algorithms Used
- **HashMaps**
  - Store word frequencies during TF-IDF computation
- **Priority Queue (Max Heap)**
  - Efficiently ranks resumes based on similarity scores
- **Sorting Algorithms**
  - Used to generate the final ordered list of candidates
- **Trie (Optional Enhancement)**
  - Enables fast keyword-based skill matching

---

## Dataset
- Source: **Kaggle Resume Dataset**
- Contains resumes across multiple job categories
- Dataset was cleaned, tokenized, and normalized before processing

---

## Performance
- **Model Accuracy:** 96%
- High relevance matching between resumes and job descriptions
- Efficient ranking even with large datasets

---

## Visualizations
The project includes visualizations for better interpretability:
- Resume relevance score distribution
- Top-ranked resume comparisons
- Keyword importance using TF-IDF weights

---

## Tech Stack
- **Language:** Python
- **Libraries:** scikit-learn, spaCy, NumPy, Pandas, Matplotlib
- **Backend (Optional):** FastAPI
- **Dataset Source:** Kaggle

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Resume-Screener-NLP-DSA.git
   cd AI-Resume-Screener-NLP-DSA
