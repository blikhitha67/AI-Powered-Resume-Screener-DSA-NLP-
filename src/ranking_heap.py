import heapq

def rank_resumes(similarity_scores, resume_ids):
    heap = []
    for i, score in enumerate(similarity_scores):
        heapq.heappush(heap, (-score, resume_ids[i]))

    ranked = []
    while heap:
        ranked.append(heapq.heappop(heap))
    return ranked

#How  It Works
#1. Uses negative values to simulate a max heap
#2. Efficiently retrieves top-ranked resumes
#3. Demonstrates core DSA (Heap) usage
