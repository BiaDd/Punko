import csv

transcript = ''

person = ''

temp = []
with open(transcript, 'r') as file:
    for line in file:
        noSpaceLine = line.strip()
        if noSpaceLine == '':
            continue
        # print(noSpaceLine)
        if noSpaceLine.isupper():
            person = noSpaceLine
        else:
            temp.append({'name': person, 'line': noSpaceLine})

with open('CSV FILE NAME', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['name', 'line'])
    writer.writeheader()
    writer.writerows(temp)

