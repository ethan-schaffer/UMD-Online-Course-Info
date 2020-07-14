import pprint
import csv

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

total_online = len(online)
total_in_person = len(in_person)
total_classes = total_online + total_in_person


print(total_online, "classes online")
print(total_in_person, "classes in person")
print(total_classes, "classes total")
print("")

percent_online = round(total_online*100 / total_classes, 2)
percent_in_person = round(total_in_person*100 / total_classes, 2)

print(str(percent_online) + "% classes online")
print(str(percent_in_person) + "% classes in person")
print("")

def get_seats_total(lst):
    total = 0
    for i in lst:
        total += int(i[4])
    return total

seats_online = get_seats_total(online)
seats_in_person = get_seats_total(in_person)
seats_total = seats_online + seats_in_person

print(seats_online, "seats online")
print(seats_in_person, "seats in person")
print(seats_total, "seats total")
print("")

percent_seats_online = round(seats_online*100 / seats_total, 2)
percent_seats_in_person = round(seats_in_person*100 / seats_total, 2)

print(str(percent_seats_online) + "% seats online")
print(str(percent_seats_in_person) + "% seats in person")
print("")

with open("summary_data.js", "w") as df:
    df.write("let total_online = '" + str(total_online) + "';\n")
    df.write("let total_in_person = '" + str(total_in_person) + "';\n")
    df.write("let total_classes = '" + str(total_classes) + "';\n")

    df.write("let percent_online = '" + str(percent_online) + "';\n")
    df.write("let percent_in_person = '" + str(percent_in_person) + "';\n")

    df.write("let seats_online = '" + str(seats_online) + "';\n")
    df.write("let seats_in_person = '" + str(seats_in_person) + "';\n")
    df.write("let seats_total = '" + str(seats_total) + "';\n")

    df.write("let percent_seats_online = '" + str(percent_seats_online) + "';\n")
    df.write("let percent_seats_in_person = '" + str(percent_seats_in_person) + "';\n")
