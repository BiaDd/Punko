import datetime
import json
import csv

# Opening JSON file
f = open('../message.json', encoding="utf8")

# returns JSON object as
# a dictionary
data = json.load(f)

messages = []

for block in data:
    dt_object = datetime.datetime.fromtimestamp(block['created_at'])
    temp = [block['sender_id'], block['name'], block['text'], dt_object]
    if temp[0] != 'system' and temp[2] != None:
        messages.append(temp)
f.close()

messages.sort(key=lambda x:x[3])

for m in messages:
    m.pop()
    print(m)