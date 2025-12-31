from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_vectors, job_vector):
    scores = cosine_similarity(resume_vectors, job_vector)
    return scores.flatten()

#How It Works
#1. Computes cosine similarity between each resume and the job description
#2. Higher score = more relevant resume
