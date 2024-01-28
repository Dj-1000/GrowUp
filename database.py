import sqlalchemy
from sqlalchemy import text
import json, os
from dotenv import load_dotenv

load_dotenv()

def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
    """Initializes a TCP connection pool for a Cloud SQL instance of MySQL."""
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.
    db_host = os.environ.get('DB_HOST') # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    db_user = os.environ.get('DB_USER') # e.g. 'my-db-user'
    db_pass = os.environ.get('DB_PASS') # e.g. 'my-db-password'
    db_name = os.environ.get('DB_NAME')  # e.g. 'my-database'
    db_port = os.environ.get('DB_PORT') # e.g. 3306

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name,
        ),
        # ...
    )
    return pool

def fetch_jobs():
    engine = connect_tcp_socket()
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
    
    result_all = result.fetchall()
    results = [tuple(row) for row in result_all]
    json_string = json.dumps(results,default=str)
    result_dicts = [row._mapping for row in result_all] 
    return result_dicts
    
    
jobs = fetch_jobs()