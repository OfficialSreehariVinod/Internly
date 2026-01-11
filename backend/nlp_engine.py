from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RoleMatcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")

    def match(self, target, jobs):
        texts = [target] + [job["description"] for job in jobs]
        tfidf = self.vectorizer.fit_transform(texts)
        scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

        for i, job in enumerate(jobs):
            job["score"] = round(float(scores[i]), 2)

        return sorted(jobs, key=lambda x: x["score"], reverse=True)
