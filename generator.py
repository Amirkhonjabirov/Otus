from json_reader import usrs
from csv_reader import books
import json


def add_apps(usr, buks):
    apps_len = len(buks)
    users_len = len(usr)

    for i, user in enumerate(usr):
        start = i * apps_len // users_len
        end = (i + 1) * apps_len // users_len
        book = buks[start: end]
        user["books"] = book


add_apps(usrs, books)

with open("result.json", "w") as f:
    s = json.dumps(usrs, indent=4)
    f.write(s)
