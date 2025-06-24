import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Set page config
st.set_page_config(page_title="DataVue - Auto EDA", page_icon="📊", layout="wide")

# App title
st.markdown("<h1 style='text-align:center;'>📊 DataVue: Auto EDA</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Upload Data")
data_source = st.sidebar.radio("Choose data source:", ("Upload CSV/XLSX", "Use Sample Dataset"), index=1)


df = None

# Upload or load dataset
if data_source == "Upload CSV/XLSX":
    uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
else:
    sample = st.sidebar.selectbox("Sample Dataset", ["Iris", "Titanic"])
    if sample == "Iris":
        df = sns.load_dataset("iris")
    elif sample == "Titanic":
        df = sns.load_dataset("titanic")

# Main App
if df is not None:
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📋 Basic Info")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.markdown("### 🏷️ Column Types")
    st.write(df.dtypes.astype(str))

    st.markdown("### 📈 Summary Statistics")
    st.write(df.describe(include='all'))

    st.markdown("### 🕳️ Missing Values per Column")
    missing = df.isnull().sum()
    st.write(missing[missing > 0])

    st.markdown("### 🔗 Correlation Matrix")
    num_df = df.select_dtypes(include=["float", "int"])
    if not num_df.empty:
        fig = px.imshow(num_df.corr(), text_auto=True, color_continuous_scale="RdBu_r")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No numeric columns available.")

    st.markdown("### 📉 Distribution Plot")
    numeric_cols = num_df.columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Select column for distribution:", numeric_cols)
        fig = px.histogram(df, x=selected_col, marginal="box", nbins=30)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No numeric column for distribution.")

    st.markdown("### 📥 Download Data")
    csv = df.to_csv(index=False)
    st.download_button("Download as CSV", data=csv, file_name="datavue_data.csv", mime="text/csv")

else:
    st.info("📂 Please upload a file or select a sample dataset.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | [GitHub](https://github.com/)")

