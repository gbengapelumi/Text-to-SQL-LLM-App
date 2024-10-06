from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load Google Gemini model and provide SQL query as a response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text


# Function to retrieve query from the SQL database
@st.cache
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except sqlite3.Error as e:
        st.error(f"An error occurred: {e}")
        return []


# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION AND MARKS \n\nFor example, \nExample 1 - How many entries or records are present?,
    the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this: SELECT * FROM STUDENT
    WHERE CLASS="Data Science";
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve any SQL Query")
st.header("Gemini App To Retrieve SQL Data")

# Sidebar with example questions
st.sidebar.markdown("### Example Questions")
st.sidebar.write(
    """
    - What is the average marks of students?
    - How many students are in Data Science?
    - Show me all students in Section A.
"""
)

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)

    # Display the generated SQL query
    st.subheader("Generated SQL Query:")
    st.code(response, language="sql")  # Show SQL code

    # Execute the SQL query
    data = read_sql_query(response, "student.db")

    st.subheader("Query Result:")
    if data:
        for row in data:
            st.write(row)
    else:
        st.write("No data found.")
