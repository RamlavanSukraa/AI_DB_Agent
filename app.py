# app/app.py
import streamlit as st
import pandas as pd
import pandasql as psql
from gpt_agent import generate_sql
from config.config import CSV_PATH

# Load the CSV data into a DataFrame
df = pd.read_csv(CSV_PATH)

# Set up the Streamlit page layout
st.set_page_config(page_title="GPT-4 SQL Data Agent", layout="wide")

# Sidebar content
st.sidebar.title("About GPT-4 SQL Data Agent")
st.sidebar.write("""
This application uses OpenAI's GPT-4 to generate SQL queries from natural language requests.
You can interact with a CSV file as if it were a SQL database.
- **Input**: Type your request in plain English.
- **Output**: The application generates a SQL query and displays the results.
- **Data Source**: The data is loaded from a CSV file.
""")

st.sidebar.header("Data Structure")
st.sidebar.write("""
The CSV file used in this app contains the following columns:
- **lab_name**: The name of the lab where tests were conducted.
- **patient_name**: Name of the patient.
- **tests**: The type of tests performed.
- **age**: Age of the patient.
- **uhid**: Unique hospital identification number.
""")

st.sidebar.header("Example Requests")
st.sidebar.write("""
- "List all patient names"
- "Show patients older than 50"
- "Count patients who had an MRI"
""")

# Main content
st.title("SQL Data Agent")
st.write("Interact with your data using natural language!")

# Show a preview of the loaded data
if st.checkbox("Show data preview"):
    st.write("Here is a preview of the data:")
    st.dataframe(df.head())

# User input for the query
user_input = st.text_area("Enter your request in natural language:", height=100)

if st.button("Submit Request"):
    if user_input:
        st.write("Generating SQL query based on your input...")
        
        # Generate the SQL query using GPT-4
        sql_query = generate_sql(user_input)
        st.markdown(f"**Generated SQL Query:**\n```sql\n{sql_query}\n```")

        try:
            # Use pandasql to run the generated SQL query on the DataFrame
            result = psql.sqldf(sql_query, {"df": df})
            
            # Display the results as a table if there are rows returned
            if not result.empty:
                st.write("Query Results:")
                st.dataframe(result)
            else:
                st.info("The query returned no results. Please try a different request.")
                
        except Exception as e:
            st.error("There was an error executing your SQL query.")
            st.error(f"Details: {e}")
    else:
        st.warning("Please enter a request before submitting.")

