import streamlit as st
import pandas as pd
from utils.predict import predict_jobs
from utils.recommender import get_career_info
from utils.plots import plot_predictions

# Load job market data
job_trends_df = pd.read_csv("data/job_market_trends.csv")

def get_job_details(role):
    row = job_trends_df[job_trends_df['Job Role'].str.lower() == role.lower()]
    if not row.empty:
        return (
            row.iloc[0]['Job Growth (%)'],
            row.iloc[0]['Average Salary (USD)'],
            row.iloc[0]['Job Market Trend'],
            row.iloc[0]['Skills in Demand']
        )
    return "No data", "No data", "No data", "No data"

# Page setup
st.set_page_config(
    page_title="Pathfinder: Personalized Career Guidance",
    page_icon="🎯",
    layout="wide"
)

# Title and description
st.markdown("### 🛤️ *Pathfinder – Apna Rasta Chuno, Sapne Sach Karo!* 🎓✨")
st.caption("Find your path, turn dreams into reality!")

st.markdown("---")

# User input section
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 Enter your name")
with col2:
    education_level = st.selectbox("🎓 Select your education level", [
        "Class 11–12 Science", "Class 11–12 Commerce", "Class 11–12 Arts",
        "Bachelor's", "Master's"
    ])

# Dynamic subject options
subject_options = {
    "Class 11–12 Science": ["physics", "chemistry", "biology", "maths", "english", "computer science"],
    "Class 11–12 Commerce": ["accountancy", "business studies", "economics", "maths", "english"],
    "Class 11–12 Arts": ["history", "geography", "political science", "psychology", "sociology", "english"],
    "Bachelor's": ["computer science", "psychology", "economics", "engineering", "design", "english", "commerce"],
    "Master's": ["data science", "mba", "education", "law", "public policy", "psychology", "finance"]
}

subjects = st.multiselect("📚 Select your subjects", subject_options.get(education_level, []))

interests = st.multiselect(
    "💡 What are your interests?",
    [
        "medicine", "engineering", "human resources", "data science", "politics",
        "arts", "business", "law", "education", "journalism", "finance",
        "marketing", "architecture", "environmental science", "psychology",
        "sports", "music", "history", "gaming"
    ]
)

st.markdown("---")

# Confirm inputs
if name and education_level and subjects and interests:
    st.success(f"Hi {name}! You're currently in **{education_level}** with interests in {', '.join(interests)} and subjects like {', '.join(subjects)}.")

    if st.button("🚀 Show Me My Career Path"):
        with st.spinner("Analyzing your profile..."):
            predictions = predict_jobs(education_level, subjects, interests)

            st.subheader("🎯 Top Career Matches")
            for job, score in predictions:
                description, course, mentor = get_career_info(job)

                st.markdown(f"### {job} ({score}%)")
                st.write(f"📝 {description}")

                if course and course != "No course available.":
                    st.write(f"🎓 [Recommended Course]({course})")

                if mentor and mentor != "No mentor available.":
                    st.write(f"🤝 [Find a Mentor]({mentor})")

                growth, salary, trend, skills = get_job_details(job)
                st.write(f"📈 Job Growth: {growth} | 💰 Avg Salary: ${salary}")
                st.write(f"📊 Trend: {trend} | 🧠 Skills: {skills}")

            # 📊 Matplotlib Prediction Chart
            st.subheader("📊 Prediction Chart")
            fig = plot_predictions(predictions)
            st.pyplot(fig)

            # ✅ Bar chart using Streamlit's built-in st.bar_chart
            st.markdown("#### 📈 Bar Chart View")
            proba_dict = dict(predictions)
            st.bar_chart(proba_dict)
else:
    st.info("Please fill out all the fields above to get your personalized recommendations.")
