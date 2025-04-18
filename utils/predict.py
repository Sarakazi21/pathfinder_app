def predict_jobs(education_level, subjects, interests):
    job_roles = {
        "Research Scientist": {
            "keywords": ["biotech", "science", "research", "biology", "chemistry"],
            "base_score": 0
        },
        "Teacher": {
            "keywords": ["teaching", "maths", "english", "history", "psychology"],
            "base_score": 0
        },
        "Graphic Designer": {
            "keywords": ["design", "arts", "english", "creativity"],
            "base_score": 0
        },
        "Entrepreneur": {
            "keywords": ["business studies", "commerce", "marketing", "entrepreneurship"],
            "base_score": 0
        },
        "Software Developer": {
            "keywords": ["coding", "computer science", "maths", "ai"],
            "base_score": 0
        },
        "Journalist": {
            "keywords": ["english", "political science", "writing", "history"],
            "base_score": 0
        },
        "Data Analyst": {
            "keywords": ["maths", "ai", "coding", "economics", "finance"],
            "base_score": 0
        }
    }

    # Normalize subjects and interests to lowercase for comparison
    input_keywords = set([s.lower() for s in subjects + interests])

    # Score jobs based on keyword matching
    job_scores = []
    for job, info in job_roles.items():
        match_count = len(set(info["keywords"]).intersection(input_keywords))
        score = match_count * 20  # Each match is worth 20%
        job_scores.append((job, score))

    # Sort by score and return top 5 matches
    job_scores = sorted(job_scores, key=lambda x: x[1], reverse=True)
    top_jobs = [(job, score) for job, score in job_scores if score > 0][:5]

    # If no job matches, return a default "Generalist"
    return top_jobs if top_jobs else [("Generalist", 10)]
