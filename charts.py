import plotly.express as px
import streamlit as st

def skill_chart(skills):

    skill_scores = {
        "Python": 90 if "python" in skills else 20,
        "SQL": 80 if "sql" in skills else 20,
        "Machine Learning": 85 if "machine learning" in skills else 20,
        "Deep Learning": 70 if "deep learning" in skills else 10,
        "Data Analysis": 80 if "pandas" in skills else 20,
        "Visualization": 70 if "tableau" in skills else 20
    }

    labels = list(skill_scores.keys())
    values = list(skill_scores.values())

    fig = px.bar(
        x=values,
        y=labels,
        orientation="h",
        text=values,
        title="Skill Analysis",
        labels={"x":"Skill Score","y":"Skills"}
    )

    fig.update_layout(
        xaxis_range=[0,100],
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)
