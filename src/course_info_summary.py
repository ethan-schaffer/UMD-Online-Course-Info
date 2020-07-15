import pprint
import csv
import json

pp = pprint.PrettyPrinter(indent=4)

dt = []
with open('output/classes.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in reader:
        dt.append(row)

dt = dt[1:]

def is_online(data_row):
    return data_row[0] == "online"

def is_in_person(data_row):
    return not is_online(data_row)

online = list(filter(is_online, dt))
in_person = list(filter(is_in_person, dt))

dept_names = {}
with open('dept_names.txt', 'r') as f:
    for line in f:
        code = line[:4] # remove linebreak which is the last character of the string
        name = line[5:-1]  # remove linebreak which is the last character of the string
        dept_names[code] = name

print(dept_names)

output_data = {}

for dept in dept_names:
    output_data[dept] = [0, 0, 0, 0]

for class_section in dt:
    print(class_section)
    dept = class_section[1]
    if is_online(class_section):
        output_data[dept][0] += 1
        output_data[dept][1] += int(class_section[4])
    else:
        output_data[dept][2] += 1
        output_data[dept][3] += int(class_section[4])

out = {}
for class_section in output_data:
    out[class_section] = {
        "departmentName": dept_names[class_section],
        "inPersonSeats": output_data[class_section][3],
        "inPersonSections": output_data[class_section][2],
        "onlineSeats": output_data[class_section][1],
        "onlineSections": output_data[class_section][0]
    }

with open("dept_summary.js", "w") as df:
    text = json.dumps(out, indent=4, sort_keys=True)

    df.write("let dept_summary = " + text + ";")