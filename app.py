import streamlit as st
import pandas as pd

st.title("Employee Salary Analysis Dashboard")

df = pd.read_csv("employee_salary_dataset (1).csv")

st.write("Dataset Preview")
st.dataframe(df.head())