import streamlit as st
from resume_parser import extract_text
from job_recommender import extract_skills
from charts import skill_chart

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Resume Analyzer", page_icon="🤖", layout="wide")

# Load CSS
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

st.title("🤖 Resume Analyzer")
st.caption("AI powered resume analysis and ML based job prediction")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

# Simple ML training data
train_text = [
    "python machine learning pandas numpy",
    "sql excel data analysis dashboard",
    "deep learning tensorflow pytorch ai"
]

train_labels = [
    "Data Scientist",
    "Data Analyst",
    "Machine Learning Engineer"
]

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_text)

model = LogisticRegression()
model.fit(X_train, train_labels)

if uploaded_file:

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    score = min(len(skills) * 12, 100)

    st.success("Resume analyzed successfully")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Resume Score")
        st.progress(score)
        st.write(f"### {score}/100")

    with col2:
        st.subheader("🧠 Skills Found")

        cols = st.columns(3)

        for i, skill in enumerate(skills):
            cols[i % 3].markdown(
                f"<div class='skill-card'>{skill.upper()}</div>",
                unsafe_allow_html=True
            )

    st.divider()

    # ML Job Prediction
    st.subheader("💼 ML Job Prediction")

    X_test = vectorizer.transform([text])

    prediction = model.predict(X_test)

    st.markdown(
        f"<div class='job-card'>Best Job Role: {prediction[0]}</div>",
        unsafe_allow_html=True
    )

    st.divider()

    # Skill Chart
    st.subheader("📊 Skill Profile")

    skill_chart(skills)

    st.divider()

    # Missing Skills
    all_skills = [
        "python","sql","machine learning",
        "deep learning","docker","kubernetes"
    ]

    missing = [s for s in all_skills if s not in skills]

    st.subheader("⚠ Missing Skills")

    for m in missing:
        st.markdown(
            f"<div class='missing-card'>{m.upper()}</div>",
            unsafe_allow_html=True
        )

    st.divider()

    # AI Resume Feedback
    st.subheader("🤖 AI Resume Feedback")

    if score < 50:
        st.error("Your resume needs improvement. Add more technical skills.")

    elif score < 80:
        st.warning("Good resume but adding advanced skills will improve job chances.")

    else:
        st.success("Excellent resume for Data Science roles.")
    
