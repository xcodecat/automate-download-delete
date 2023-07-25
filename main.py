import os
import time
import shutil


def main():
    path = input("Enter a valid absolut path (defaults to $HOME/Downloads/): ") or os.getenv("HOME") + "/Downloads/"
    now = time.time()
    times = {'days': 86400, 'hours': 3600, 'minutes': 60}
    time_period = input("Enter desired time period (e.g. days, hours, minutes): ")

    if time_period not in times:
        print("Invalid time period entered. Please choose from 'days', 'hours', or 'minutes'!")
        exit()

    duration = int(input(f"Enter the number of {time_period} for considering file deletion (e.g. 7): "))

    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.stat(f).st_mtime < now - duration * times.get(time_period):
            if os.path.isfile(f):
                os.remove(os.path.join(path, f))
            elif os.path.isdir(f):
                shutil.rmtree(f)


if __name__ == "__main__":
    main()
