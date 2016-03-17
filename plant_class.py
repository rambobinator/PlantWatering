import csv
from datetime import datetime, timedelta
import os

class Plant:
    """Plant actions"""
    def __init__(self, db_entry, log_filename="Default"):
        self.log_filename = log_filename
        self.id = db_entry[0]
        self.type = db_entry[1]
        self.temperature = db_entry[2]
        self.location = db_entry[3]
        self.frequency = int(db_entry[4])
        self.webhook = db_entry[5]

    def log(self, data):
        with open(self.log_filename, "a+") as f:
                f.write("{}\n".format(data))

    def watering_need(self, current_date):
        """ Return last watering time if plant deserve water or None"""
        with open(self.log_filename, 'rb') as fh:
            for line in fh:
                pass
            last_watering = datetime.strptime(line.decode().rstrip(), "%Y-%m-%d")
            if (last_watering + timedelta(days=self.frequency)) < current_date:
                # Here we suppose that plants are gonna be watering ...
                # but we can't think about a better solution to check they are.
                # maybe Qrcode.
                self.log(datetime.strftime(current_date, "%Y-%m-%d"))
                return last_watering
        return None
