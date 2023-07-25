import os
import time
import shutil

path = input("Enter a valid absolut path (e.g. /home/xcodecat/Downloads/): ")
now = time.time()

time_period = input("Enter desired time period (e.g. days, hours, minutes): ")

if time_period == "days":
    duration_text = "days"
elif time_period == "hours":
    duration_text = "hours"
elif time_period == "minutes":
    duration_text = "minutes"
else:
    print("Invalid time period entered. Please choose from 'days', 'hours', or 'minutes'!")
    exit()

duration = int(input(f"Enter the number of {duration_text} for considering file deletion (e.g. 7): "))

if time_period == "days":
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.stat(f).st_mtime < now - duration * 86400:
            if os.path.isfile(f):
                os.remove(os.path.join(path, f))
            elif os.path.isdir(f):
                shutil.rmtree(f)
elif time_period == "hours":
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.stat(f).st_mtime < now - duration * 3600:
            if os.path.isfile(f):
                os.remove(os.path.join(path, f))
            elif os.path.isdir(f):
                shutil.rmtree(f)
elif time_period == "minutes":
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.stat(f).st_mtime < now - duration * 60:
            if os.path.isfile(f):
                os.remove(os.path.join(path, f))
            elif os.path.isdir(f):
                shutil.rmtree(f)
