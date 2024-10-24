# database/db_manager.py
from sqlalchemy import create_engine, text
from config.config import DATABASE_URL

# Setup database engine
engine = create_engine(DATABASE_URL)

def execute_query(sql_query: str):
    """
    Execute an SQL query and fetch results.
    :param sql_query: The SQL query to execute.
    :return: Query results or a success message.
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))
            if result.returns_rows:
                return result.fetchall()
            return "Query executed successfully."
    except Exception as e:
        return f"Error executing query: {str(e)}"
