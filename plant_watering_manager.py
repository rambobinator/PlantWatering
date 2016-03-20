#!/usr/bin/env python2.7
# coding: utf8
import csv
from datetime import datetime
import os

from plant_class import *

DB = "plant_db.csv"
DB_TEMPLATE = "id,type,temperature(celsius),Location(level-room_name),Frequency(in days),mattermost_webhook"
LOG_PATH = "log/"


if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
if not os.path.exists(DB):
    with open(DB, "a+") as f:
        f.write("{}\n".format(DB_TEMPLATE))
        print("{} was just created".format(DB))


with open(DB, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    current_date = datetime.now()
    for line in reader:
        log_filename = "{}{}_{}".format(LOG_PATH, line[1], line[0])
        if not os.path.exists(log_filename):
            with open(log_filename, "a+") as f:
                f.write("{}\n".format(datetime.strftime(current_date, "%Y-%m-%d")))
        plant = Plant(line, log_filename)
        res = plant.watering_need(current_date)
