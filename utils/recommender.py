# utils/recommender.py

import pandas as pd

def get_career_info(job_role):
    # Load and clean column names from CSV files
    desc_df = pd.read_csv('data/career_descriptions.csv')
    course_df = pd.read_csv('data/Course_links.csv')
    mentor_df = pd.read_csv('data/Mentor_links.csv')

    # Strip leading/trailing spaces from column names
    desc_df.columns = desc_df.columns.str.strip()
    course_df.columns = course_df.columns.str.strip()
    mentor_df.columns = mentor_df.columns.str.strip()

    # Safely extract the career-related details
    desc = desc_df.loc[desc_df['Career'] == job_role, 'Description'].values
    course = course_df.loc[course_df['Career'] == job_role, 'Course_link'].values
    mentor = mentor_df.loc[mentor_df['Career'] == job_role, 'Mentor_link'].values

    # Return career description, course link, and mentor link (if available)
    return (
        desc[0] if len(desc) > 0 else "No description available.",
        course[0] if len(course) > 0 else "No course available.",
        mentor[0] if len(mentor) > 0 else "No mentor available."
    )
