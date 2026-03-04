kills_list = [
"python","sql","machine learning","deep learning",
"pandas","numpy","tensorflow","docker","kubernetes",
"excel","power bi","tableau","data analysis"
]

def extract_skills(text):

    found_skills = []
    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def recommend_jobs(skills):

    jobs = []

    if "machine learning" in skills:
        jobs.append("Machine Learning Engineer")

    if "python" in skills and "pandas" in skills:
        jobs.append("Data Scientist")

    if "sql" in skills:
        jobs.append("Data Analyst")

    if "tableau" in skills or "power bi" in skills:
        jobs.append("Business Intelligence Analyst")

    if not jobs:
        jobs.append("General Software / Data Role")

    return jobs
