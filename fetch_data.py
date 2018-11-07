import psycopg2
from config import DB_CONNECTION_STRING
import json
from pprint import pprint
import random

# Setup database connection
connection = psycopg2.connect(DB_CONNECTION_STRING)
client = connection.cursor()

# Run query to get responses
NAME = 0
RESULT = 1
client.execute("SELECT name, result FROM results;")

# Commit the transaction
connection.commit()

# Get the results
res = client.fetchall()

# Format
results = {}
for row in res:
        results[row[NAME]] = row[RESULT]

pprint(results)