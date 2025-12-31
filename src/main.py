from preprocessing import clean_text
from tfidf_vectorizer import get_tfidf_vectors
from similarity import calculate_similarity
from ranking_heap import rank_resumes

resumes = [clean_text(r) for r in resume_texts]
job_desc = clean_text(job_description)

documents = resumes + [job_desc]

tfidf_matrix, _ = get_tfidf_vectors(documents)

resume_vectors = tfidf_matrix[:-1]
job_vector = tfidf_matrix[-1]

scores = calculate_similarity(resume_vectors, job_vector)
ranked_resumes = rank_resumes(scores, resume_ids)

#How it works
#1. Cleans resumes and job description
#2. Converts text to TF-IDF vectors
#3. Calculates similarity scores
#4. Ranks resumes using a heap
