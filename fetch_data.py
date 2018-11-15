import psycopg2
from config import DB_CONNECTION_STRING
import csv
import pandas as pd

def song_id_to_song_name(id_string):
    if id_string == '0':
        return "Forest"
    elif id_string == '1':
        return "Harsh"
    elif id_string == '2':
        return "Street"
    else:
        return ""


def get_results_dataframe():
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

    with open('results.csv', 'w', newline='') as file:
        labels = ["ID", "Musician Type", "Song", "Start", "End", "Label"]
        writer = csv.DictWriter(file, fieldnames=labels)

        # Column labels
        writer.writeheader()

        for row in res:
            id = row[NAME]
            if id in ["903337531", "903165064", "903339825", "902946528"]:
                musician_type = "Percussionist"
            else:
                musician_type = "Instrumentalist"
            for song in row[RESULT]:
                song_name = song_id_to_song_name(song)
                for region in row[RESULT][song]:
                    writer.writerow(dict(zip(labels, [id, musician_type, song_name, region["start"], region["end"], region["label"]])))

    return pd.read_csv('results.csv')
