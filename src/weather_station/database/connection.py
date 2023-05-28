import psycopg2
from pathlib import Path
from dotenv import load_dotenv
import os


def get_connection():
    """Returns a connection to the database

    The database connection parameters are configured in the project root .env
    file.

    Returns:
        psycopg2.connection: Database connection
    """
    load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")

    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    connection = psycopg2.connect(
        host=db_host, port=db_port, database=db_name, user=db_user,
        password=db_password
    )

    return connection
