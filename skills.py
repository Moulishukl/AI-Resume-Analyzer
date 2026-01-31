skills_list = [
    "python", "java", "sql", "machine learning",
    "data analysis", "html", "css", "javascript",
    "react", "power bi", "excel", "nlp", "deep learning"
]

def extract_skills(text):
    text = text.lower()
    found_skills = [skill for skill in skills_list if skill in text]
    missing_skills = [skill for skill in skills_list if skill not in text]
    return found_skills, missing_skills
