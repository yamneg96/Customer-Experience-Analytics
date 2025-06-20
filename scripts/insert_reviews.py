import pandas as pd
from dotenv import load_dotenv
import os
import sys
from pathlib import Path

# Add the project root directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from src.db import insert_reviews

# Load environment variables for Oracle connection
load_dotenv()
user = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
dsn = os.getenv("ORACLE_DSN")

# Load cleaned reviews
df = pd.read_csv("data/bank_reviews_clean.csv")

# Insert into Oracle DB
insert_reviews(df, user, password, dsn)
print("Inserted cleaned reviews into Oracle database.")