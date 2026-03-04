skills_list = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "tableau",
    "power bi",
    "excel"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return found_skills
