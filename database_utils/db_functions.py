from sqlalchemy import create_engine
import pandas as pd
from database_utils import db

def get_engine():
    connection_str = f"{db['dialect']}+{db['driver']}://{db['username']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
    engine = create_engine(connection_str, echo=True)
    return engine

def query_to_df(sql_query):
    """
    Execute an SQL query and return the results as a Pandas DataFrame.

    Parameters:
    - sql_query: A string containing the SQL query to be executed.
    - db_url: A string with the database URL in SQLAlchemy format.

    Returns:
    - A Pandas DataFrame containing the results of the SQL query.
    """
    engine = get_engine()
    # Use pandas to execute the query and return the results as a DataFrame
    df = pd.read_sql_query(sql_query, con=engine)
    
    # Close the database engine
    engine.dispose()
    
    return df