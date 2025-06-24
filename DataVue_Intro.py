
import streamlit as st
from streamlit.components.v1 import html

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
        background-color: #1e90ff;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 25px;
        text-align: center;
        margin: 10px;
        display: inline-block;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .app-button:hover {
        background-color: #4169e1;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
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
    </style>
    """, unsafe_allow_html=True)

def main():
    load_css()

    # Main title and tagline with emojis
    st.markdown("<h1 class='main-title'>📊 DataVue 🔍</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tagline'>\"Your Data, Your View\" 🚀</p>", unsafe_allow_html=True)

    # Problem Statement
    st.markdown("""
    <div class='problem-statement'>
        <h3>🤔 Struggling with data analysis?</h3>
        <p>Drowning in data but starving for insights? Tired of complex tools and steep learning curves?</p>
        <h3>💡 DataVue is your solution!</h3>
    </div>
    """, unsafe_allow_html=True)

    # Why choose DataVue section
    st.markdown("<h2 class='section-header'>🌟 Why Choose DataVue?</h2>", unsafe_allow_html=True)

    features = [
        {
            "title": "🔬 Complete Data Analysis",
            "description": "Experience effortless data analysis with DataVue. Simply provide your data, and let our advanced algorithms handle the rest, delivering comprehensive insights at your fingertips."
        },
        {
            "title": "🤖 AI Assistant for Data Science",
            "description": "Access a powerful AI assistant dedicated to all your data science tasks. Get instant help, explanations, and curated resources to supercharge your data science journey."
        },
        {
            "title": "📊 Automated EDA",
            "description": "Unlock the power of automated Exploratory Data Analysis (EDA) with SweetViz and Pandas Profiling. Generate in-depth reports and visualizations with just a few clicks, saving you time and effort."
        },
        {
            "title": "📚 Comprehensive Learning Resources",
            "description": "Embark on a data science learning adventure from zero to hero. Access a wealth of study materials covering EDA, missing value handling, feature engineering, scaling transformations, and ML algorithms - all in one place, complete with example datasets and practical demos."
        }
    ]

    for feature in features:
        st.markdown(f"""
        <div class='feature-box'>
            <p class='feature-title'>{feature['title']}</p>
            <p>{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
