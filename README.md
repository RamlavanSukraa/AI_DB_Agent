
# SQL Data Agent with GPT-4

This project provides a way to interact with a PostgreSQL database using SQL queries generated from natural language inputs through GPT-4. It uses **Streamlit** to offer a user-friendly web interface, making it easy for non-technical users to query and manage data without needing SQL expertise.

## Features

- Accepts natural language input to interact with a PostgreSQL database.
- Translates natural language into SQL queries using GPT-4.
- Executes generated SQL queries directly on the PostgreSQL database.
- Displays the generated SQL query and the resulting data on a Streamlit-based interface.
- Supports easy integration with various data tables and database structures.

## Project Structure

```
📦 SQL_Data_Agent/
├── 📄 app.py                       # Main Streamlit application.
│
├── 📂 config/
│   ├── 📄 config.ini               # Configuration file for database URL and OpenAI API key.
│   └── 📄 config.py                # Reads and parses configuration from config.ini.
│
├── 📂 database/
│   ├── 📄 db_manager.py            # Manages database connections and executes SQL queries.
│   ├── 📄 Mock_Patient_Data.csv    # Example CSV file for testing (optional).
│
├── 📄 gpt_agent.py                 # Logic for generating SQL queries using GPT-4.
├── 📄 test_connection.py           # Script to test database connectivity.
├── 📄 requirements.txt             # Python dependencies.
└── 📄 README.md                    # Project documentation.

```

## Prerequisites

Ensure you have the following installed:

- **Python 3.7+**.
- A **PostgreSQL Database** with user access.
- An **OpenAI API Key** (sign up at [OpenAI](https://beta.openai.com/signup/)).
- **Streamlit** for the user interface.
- **psycopg2** and **SQLAlchemy** for PostgreSQL database connectivity.

## Setup and Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/RamlavanSukraa/AI_DB_Agent.git
cd AI_DB_Agent
```

### Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 3: Configure the Application

Edit `config/config.ini` to include your database connection details and OpenAI API key:

```ini
[openai]
api_key = YOUR_OPENAI_API_KEY

[database]
url = postgresql+psycopg2://username:password@host:port/database_name
```

- Replace `YOUR_OPENAI_API_KEY` with your OpenAI API key.
- Adjust `username`, `password`, `host`, `port`, and `database_name` to match your PostgreSQL setup.

### Step 4: Database Setup

1. Ensure that your PostgreSQL server is running.
2. Create the necessary table structure. Example:

   ```sql
   CREATE TABLE data_table (
       column1 VARCHAR(255),
       column2 INT,
       column3 TEXT
   );
   ```

   Use **psql** or **pgAdmin** to create the table.

### Step 5: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Access the app at `http://localhost:8501`.

## Using the Application

1. Input a natural language query in the provided text box:
   - Examples:
     - `"List all entries in column1"`
     - `"Count records where column2 is greater than 10"`
     - `"Show all entries containing 'keyword' in column3"`
2. The app generates a SQL query using GPT-4.
3. The generated SQL and results are displayed on the web interface.

### Example Query:

- **Input**: `"List all items where column2 is greater than 5"`
- **Generated SQL Query**: 
  ```sql
  SELECT * FROM data_table WHERE column2 > 5;
  ```
- **Result**: A table with the relevant data.

## Project Files Overview

### 1. `app.py`
Handles the main application logic, including user input, SQL query generation, and displaying results using Streamlit.

### 2. `config/config.ini` & `config/config.py`
- **`config.ini`**: Stores API keys and database connection strings.
- **`config.py`**: Loads and makes these configurations available to the application.

### 3. `database/db_manager.py`
Facilitates interactions with the PostgreSQL database:
- Manages connection setup.
- Provides functions to execute SQL commands.

### 4. `gpt_agent.py`
Handles the interaction with GPT-4 to generate SQL queries from user prompts.

### 5. `test_connection.py`
A utility script to test database connectivity before running the main application.

### 6. `requirements.txt`
Specifies all dependencies, including:

- `openai` for GPT-4 API access.
- `sqlalchemy` for database ORM.
- `psycopg2-binary` for PostgreSQL connectivity.
- `streamlit` for web-based interactions.

## Troubleshooting

- **Issue**: `relation "data_table" does not exist`
  - **Solution**: Ensure that the specified table exists in the database.

- **Issue**: `Invalid OpenAI API Key`
  - **Solution**: Confirm that your API key is correctly configured in `config.ini`.

- **Issue**: `psycopg2.errors.UndefinedTable`
  - **Solution**: Verify that the table name matches the one used in the generated SQL queries.

## Customization

### Change Table Structure:
Adjust `gpt_agent.py` to include new table structures or column names as needed.

### Switch Database:
Update the `DATABASE_URL` in `config.ini` to connect to a different database.

### Change GPT Model:
To use a different OpenAI model, update the `MODEL` variable in `gpt_agent.py`.

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Acknowledgments

- Special thanks to OpenAI for the GPT-4 API.
- Inspired by the need to simplify SQL access for non-technical users.
- Thanks to the open-source community for making projects like this possible.
