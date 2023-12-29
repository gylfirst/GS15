# Module de la gestion des dates


def get_date():
    import time

    current_timestamp = int(time.time())
    # print("Current Timestamp:", current_timestamp)

    return current_timestamp


def get_exp_date(date):
    from datetime import datetime, timedelta

    # Convert the timestamp to a datetime object
    date_time = datetime.utcfromtimestamp(date)

    # Add 3 months
    new_date_time = date_time + timedelta(days=3*30)

    # Convert to Unix timestamp
    new_timestamp = int(new_date_time.timestamp())

    # print("Original Timestamp:", int(current_date_time.timestamp()))
    # print("Timestamp after adding 3 months:", new_timestamp)

    return new_timestamp
