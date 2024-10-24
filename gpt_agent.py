import openai
from config.config import OPENAI_API_KEY

# Setup OpenAI API key
openai.api_key = OPENAI_API_KEY
MODEL = "gpt-4"

def generate_sql(user_input: str) -> str:
    """
    Generate SQL query based on user input using GPT-4.
    :param user_input: A natural language description of what the user wants.
    :return: Generated SQL query as a string.
    """
    prompt = f"""
    You are a helpful assistant that generates SQL queries.
    User Input: {user_input}
    Assume that the table is named 'patient_data' and contains columns: 'lab_name', 'patient_name', 'tests', 'age', 'uhid'.
    Write a SQL query that fulfills the user's request.
    """
    
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "system", "content": "You generate SQL queries based on user inputs."},
                  {"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.2
    )
    
    sql_query = response['choices'][0]['message']['content'].strip()
    return sql_query
