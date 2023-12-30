# Module de la gestion des dates

import time
from datetime import datetime, timedelta

# Recupère la date d'aujourd'hui
def get_date():
    current_timestamp = int(time.time())
    # print("Current Timestamp:", current_timestamp)

    return current_timestamp


# Récupère la date donnée et l'avance de 3 mois
def get_exp_date(date):
    # Convert the timestamp to a datetime object
    date_time = datetime.utcfromtimestamp(date)

    # Add 3 months
    new_date_time = date_time + timedelta(days=3*30)

    # Convert to Unix timestamp
    new_timestamp = int(new_date_time.timestamp())

    # print("Original Timestamp:", int(current_date_time.timestamp()))
    # print("Timestamp after adding 3 months:", new_timestamp)

    return new_timestamp
