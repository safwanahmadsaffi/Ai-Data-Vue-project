import streamlit as st
import requests

def load_css():
    st.markdown("""
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    .main-title {
        color: #1e90ff;
        font-size: 72px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .tagline {
        color: #4169e1;
        font-size: 28px;
        font-style: italic;
        text-align: center;
        margin-bottom: 30px;
    }
    .section-header {
        color: #1e90ff;
        font-size: 36px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 20px;
        text-align: center;
    }
    .feature-box {
        background-color: #e6f2ff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.3s ease-in-out;
    }
    .feature-box:hover {
        transform: scale(1.05);
    }
    .feature-title {
        color: #4169e1;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .app-button {
        background-color: white;
        color: #1e90ff;
        font-size: 12px;
        font-weight: bold;
        padding: 8px 16px;
        border-radius: 25px;
        text-align: center;
        margin: 5px;
        display: inline-block;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 1px solid #1e90ff;
    }
    .app-button:hover {
        background-color: #FFD35A;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .problem-statement {
        background-color: #ffd700;
        border-radius: 10px;
        padding: 20px;
        margin: 30px 0;
        text-align: center;
        font-size: 20px;
        color: #333;
    }
    .circular-image {
        border-radius: 50%;
        overflow: hidden;
        width: 120px;
        height: 120px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #1e90ff;
        margin: auto;
    }
    .circular-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>
    """, unsafe_allow_html=True)

def new_line():
    st.markdown("<br>", unsafe_allow_html=True)

# Create the About Us page
def about_page():
    load_css()  # Load custom CSS

    # Title Page
    st.markdown("<h1 class='main-title'> 🔎 About Us - Data Vue</h1>", unsafe_allow_html=True)
    new_line()

    # About the Project
    st.markdown("""
    <div class='tagline'>Welcome to Data Vue!</div>
    <p>Welcome to Data Vue! This application is designed to provide a comprehensive platform for data analysis and machine learning.
    Whether you're a beginner or an experienced data scientist, our tool is tailored to simplify your workflow.</p>
    """, unsafe_allow_html=True)
    new_line()

    st.markdown("<h2 class='section-header'>👤 Meet the Team</h2>", unsafe_allow_html=True)

    # Define the team members with GitHub links
    team_members = [
        {"name": "Ahmad", "role": "Data Scientist", "image": "ali.jpg", "github": "https://github.com/safwanahmadsaffi"},
        {"name": "Safwan", "role": "Frontend Developer", "image": "sara.jpg", "github": "https://github.com/safwanahmadsaffi"},
        {"name": "Umeer", "role": "ML Engineer", "image": "zain.jpg", "github": "https://github.com/safwanahmadsaffi"}
    ]

    cols = st.columns(len(team_members))

    # Populate each column with a team member's details
    for col, member in zip(cols, team_members):
        with col:
            st.markdown(f"""
                <div class='circular-image'>
                    <img src='{member["image"]}' />
                </div>
                <div class='feature-box' style='text-align:center'>
                    <strong>{member['name']}</strong><br>
                    <em>{member['role']}</em><br>
                    <a href="{member['github']}" target="_blank" class="app-button">GitHub</a>
                </div>
            """, unsafe_allow_html=True)

    new_line()

    # What this app does
    st.markdown("<h2 class='section-header'>What This App Does</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='feature-box'>
        <h3>👉 Data Vue Intro</h3>
        <p>This section provides a comprehensive introduction to Data Vue, explaining its purpose and the key features it offers for data analysis and machine learning.</p>
    </div>
    <div class='feature-box'>
        <h3>👉 Click DataVue</h3>
        <p>This section is the main page of the *Click DataVue* web app. It provides the customizability to build Machine Learning models by selecting and applying the Data Preparation techniques that fit your data. Also, you can try different Machine Learning models and tune the hyperparameters to get the best model.</p>
    </div>
    <div class='feature-box'>
        <h3>📊 EDA with AI</h3>
        <p>This section focuses on Exploratory Data Analysis (EDA) powered by AI. It helps users to discover insights, identify patterns, and visualize data effectively using AI-driven methods.</p>
    </div>
    <div class='feature-box'>
        <h3>🚀 Quick DataVue</h3>
        <p>Data Vue is a tab that allows you to build a model quickly with just a few clicks. This tab is designed for people who are new to Machine Learning and want to build a model quickly without having to go through the entire process of Exploratory Data Analysis, Data Cleaning, Feature Engineering, etc. It is just a quick way to build a model for testing purposes.</p>
    </div>
    <div class='feature-box'>
        <h3>🤖 Assistant AI</h3>
        <p>The Assistant AI offers personalized support and guidance. It helps with real-time coding assistance, document summarization, interactive study planning, and more, tailoring its responses to your needs.</p>
    </div>
    <div class='feature-box'>
        <h3>📚 Study DataVue</h3>
        <p>The StudyML tab is designed to help you understand the key concepts of building machine learning models. This tab has 7 sections, each section talking about a specific concept in building machine learning models. With each section, you will have the ability to apply the concepts of these sections on multiple datasets. The code, the explanation, and everything you need to understand is in this tab.</p>
    </div>
    """, unsafe_allow_html=True)
    new_line()


if __name__ == "__main__":
    about_page()
