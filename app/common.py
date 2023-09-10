import json
from importlib.resources import open_text

with open_text('app.resources', 'data.json') as file:
    DATASET = json.loads(file.read())

with open_text('app.resources', 'qset.json') as file:
    QSET = json.loads(file.read())
