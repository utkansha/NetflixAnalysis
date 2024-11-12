import streamlit as st
import pandas as pd

df = pd.read_csv("netflix_titles.csv", index_col=0)

# Title and Introduction
st.title("Netflix Titles Exploration")
st.write("This app allows you to explore various aspects of the Netflix titles dataset.")

# Sidebar for User Selection
selected_type = st.sidebar.selectbox("Select Content Type", df["type"].unique())
selected_country = st.sidebar.selectbox("Select Country (Optional)", df["country"].unique(), key="country")

# Filter Data based on selections
filtered_df = df.copy()
if selected_type:
    filtered_df = filtered_df[filtered_df["type"] == selected_type]
if selected_country:
    filtered_df = filtered_df[filtered_df["country"] == selected_country]

# Display Top 10 Directors (if 'director' column exists)
if "director" in filtered_df.columns:
    top_directors = filtered_df["director"].value_counts().iloc[1:11]
    st.subheader("Top 10 Directors")
    st.bar_chart(top_directors)

# Display Top 10 Release Years (if 'release_year' column exists)
if "release_year" in filtered_df.columns:
    top_release_years = filtered_df["release_year"].value_counts().head(10)
    st.subheader("Top 10 Release Years")
    st.bar_chart(top_release_years)

# Display Dataframe (Head or Sample)
st.subheader("Data Preview")
data_view = st.radio("View", ("Head", "Sample 100"))
if data_view == "Head":
    st.dataframe(filtered_df.head())
else:
    st.dataframe(filtered_df.sample(100))

# Display Specific Content based on User Selection (Example)
if selected_type == "Movie" and selected_country == "Egypt":
    egypt_movies = filtered_df.query("type == 'Movie' and country == 'Egypt'")
    st.subheader("Egyptian Movies")
    st.dataframe(egypt_movies)

# Add more functionalities based on your specific interests in the data (e.g., histograms, correlations)

st.stop()
