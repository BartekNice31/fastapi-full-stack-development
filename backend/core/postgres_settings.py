from pathlib import Path
import os
from dotenv import load_dotenv

path_env=Path('..')/'.env'
load_dotenv(path_env)

class PostgresSettings:
    POSTGRES_USER:str=os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD:str=os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER:str=os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT:str=os.getenv("POSTGRES_PORT")
    PORTGRES_DB:str=os.getenv("POSTGRES_DB")
    
postgressettings=PostgresSettings()