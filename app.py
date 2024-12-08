import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="Simple Streamlit Demo",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Simple Streamlit Demo")

# Sidebar
st.sidebar.header("Settings")
n_points = st.sidebar.slider("Number of points", 10, 1000, 100)

# Main content
st.header("Interactive Data Visualization")

# Generate random data
data = pd.DataFrame({
    'x': np.random.randn(n_points),
    'y': np.random.randn(n_points)
})

# Display the scatter plot
st.subheader("Random Scatter Plot")
st.scatter_chart(data, x='x', y='y')

# Display statistics
st.subheader("Data Statistics")
col1, col2 = st.columns(2)

with col1:
    st.metric("X Mean", f"{data['x'].mean():.2f}")
    st.metric("X Std", f"{data['x'].std():.2f}")

with col2:
    st.metric("Y Mean", f"{data['y'].mean():.2f}")
    st.metric("Y Std", f"{data['y'].std():.2f}")

# Show raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(data)