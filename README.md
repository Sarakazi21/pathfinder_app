

📄 README.md (for Pathfinder App)

# Pathfinder: Personalized Academic & Career Guidance App

Pathfinder is a Streamlit-powered web application designed to help students explore personalized career and academic paths based on their interests, subjects, passions, and educational background. It uses data science and machine learning techniques to predict suitable job roles, suggest relevant courses and mentors, visualize results, and guide users with smart career insights.

🚀 Features

- 🎯 Personalized career predictions based on education level, subjects, and hobbies
- 📊 Career probability charts and visual summaries
- 📚 Curated course recommendations (e.g., Coursera, edX)
- 🧑‍🏫 Mentorship suggestions via platforms like LinkedIn and ADPList
- 💬 Chatbot-style career assistant (streamlit_chat)
- 📄 PDF export of recommendations
- 📈 Learns from user inputs over time (self-learning logic)
- ✅ Supports Class 8–10, 11–12 (Science/Commerce/Arts), Bachelors, and Masters

🗂️ Folder Structure

pathfinder/
│
├── app.py                        # Main Streamlit app entry point
├── model/
│   ├── train_model.py           # Code to train/update the ML model
│   ├── model.pkl                # Trained job prediction model
│   └── job_subject_mapping.csv  # Dataset mapping subjects to job roles
│
├── data/
│   ├── user_logs.csv            # CSV logging user inputs and predictions
│   ├── subject_list.csv         # List of subjects for each education level
│   └── hobby_list.csv           # List of hobbies and mapped career domains
│
├── utils/
│   ├── prediction.py            # Logic for predicting careers
│   ├── recommender.py          # Logic for suggesting courses & mentors
│   ├── visualization.py        # Generates probability graphs and charts
│   ├── pdf_export.py           # Exports results to PDF
│   └── chatbot_logic.py        # Smart assistant logic (streamlit_chat)
│
├── assets/
│   ├── icons/                   # Icons or illustrations used in UI
│   └── style.css                # Optional custom styling
│
├── requirements.txt            # Python dependencies for the app
└── README.md                   # Project overview and setup instructions

🔧 Installation & Setup

1. Clone the repository:
   git clone https://github.com/your-username/pathfinder.git  
   cd pathfinder

2. Create a virtual environment and install requirements:
   python -m venv venv  
   source venv/bin/activate  # on Windows use `venv\Scripts\activate`  
   pip install -r requirements.txt

3. Launch the Streamlit app:
   streamlit run app.py

🧠 Tech Stack

- Python
- Streamlit
- Pandas / NumPy
- scikit-learn
- Matplotlib / Seaborn
- fpdf / ReportLab (for PDF export)

📌 To-Do

- Add user authentication & save profiles
- Enhance chatbot with more NLP features
- Integrate real-time job market trends via APIs
- Build an admin dashboard for analytics

👩‍💻 Maintained By

Sara Kazi  
MSc Data Science & AI – Semester 4  
Project: Pathfinder – A Personalized Guidance Platform

📬 Contact

For queries or collaboration: sara.taufique@gmail.com

