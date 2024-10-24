from sqlalchemy import create_engine, text
from config.config import DATABASE_URL

def test_connection():
    try:
        # Create an engine to connect to the PostgreSQL database
        engine = create_engine(DATABASE_URL)
        
        # Try to establish a connection
        with engine.connect() as conn:
            # Execute a simple query to verify the connection
            result = conn.execute(text("SELECT 1"))
            print("Database connection successful!")
            for row in result:
                print(f"Result: {row[0]}")
                
    except Exception as e:
        print("Error connecting to the database.")
        print(f"Details: {e}")

if __name__ == "__main__":
    test_connection()
