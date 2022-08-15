import json

with open('users.json', 'r') as f:
    users = json.loads(f.read())

usrs = []
for user in users:
    tmp = {
        'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'age': user['age']

    }
    usrs += [tmp]
