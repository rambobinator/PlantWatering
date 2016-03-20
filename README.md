# PlantWatering
A plant watering notifier writed in python, for dreamy coworkers ...

* Fisrt of all:
```
python plant_watering_manager.py
```
That will create corrects files and directories.

* Then edit db_plant.csv, and fill it using the header shema:

example:

```
cat plant_db.csv
id,type,temperature(celsius),Location(level-room_name),Frequency(in days),mattermost_webhook
1,bonzai,25,1-MY_TEAM,15,https://mattermost.MY_COMPANY.com/hooks/TOKEN
```

where:

+ id,           is the plant unique identifier
+ type,         is the plant type (bonsai, cactus, dracaena ...)
+ temperature,  is the ideal temperature for the plant growth in degree celsius
+ location,     is the place where is located the plante (FLOOR_LVL-OFFICE) ex: (4-FINANCIAL)
+ frequency,    is the ideal watering frequency for the plant growth
+ webhook,      is your mattermost/slack URL webhook

Then you could make use of CRON to call this script daily, and it will notify everyone to take care of plants.
