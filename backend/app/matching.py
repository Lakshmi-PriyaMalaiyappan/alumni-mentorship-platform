from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _text(skills, extra=""):
    return " ".join(s.replace(" ", "_").lower() for s in skills) + " " + extra.lower()


def match_mentors(student, alumni, top_n=3):
    """Rank alumni by TF-IDF cosine similarity with the student's profile."""
    student_text = _text(student.get("skills", []) + student.get("interests", []), student.get("target_role", ""))
    docs = [_text(a["skills"], a["role"] + " " + a["domain"]) for a in alumni]
    vec = TfidfVectorizer(token_pattern=r"[^\s]+")
    m = vec.fit_transform(docs + [student_text])
    scores = cosine_similarity(m[-1], m[:-1])[0]
    ranked = sorted(zip(alumni, scores), key=lambda x: x[1], reverse=True)[:top_n]
    return [{**a, "match_percent": round(float(s) * 100, 1)} for a, s in ranked]
