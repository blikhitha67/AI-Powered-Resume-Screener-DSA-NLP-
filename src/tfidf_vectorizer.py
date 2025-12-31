from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_vectors(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    return tfidf_matrix, vectorizer

#How It Works
#1. Transforms resumes and job description into TF-IDF vectors
#2. Captures keyword importance across documents
