from bs4 import BeautifulSoup
import requests
import pprint
import csv

import json

pp = pprint.PrettyPrinter(indent=4)

umd_departments = []

with open('dept_codes.txt', 'r') as f:
    for line in f:
        currentPlace = line[:-1] # remove linebreak which is the last character of the string
        umd_departments.append(currentPlace)

def get_in_person(dept):
    return "https://app.testudo.umd.edu/soc/search?courseId=" + dept + "&sectionId=&termId=202008&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&facetoface=true&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"

def get_online(dept):
    return "https://app.testudo.umd.edu/soc/search?courseId=" + dept + "&sectionId=&termId=202008&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&online=true&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"

def get_count(url, split_string):
    dt = {}
    course_capcities = []
    data = requests.get(url).content
    soup = BeautifulSoup(data, 'html.parser')
    courses = soup.findAll("div", {"class": "course"})
    for course in courses:
        course_id = course.get("id")
        dt[course_id] = {}
        rows = course.findAll("div", {"class": "row"})
        for row in rows:
            info_containers = row.findAll("div", {"class": "course-info-container eleven columns"})
            for info_container in info_containers:
                link_containers = info_container.findAll("div", {"class": "toggle-sections-link-container"})
                for link_container in link_containers:
                    row_containers = link_container.findAll("div", {"class": "row"})
                    for row_container in row_containers:
                        column_containers = row_container.findAll("div", {"class:", "sections-fieldset-container twelve columns"})
                        for column_container in column_containers:
                            displayed_sections = column_container.findAll("fieldset", {"class:",
                                                                              "sections-fieldset sections-displayed"})
                            for displayed_section in displayed_sections:
                                sections_containers = displayed_section.findAll("div", {"class:",
                                                                                  "sections-container"})
                                for sections_container in sections_containers:
                                    sixteen_colgrids = sections_container.findAll("div", {"class:",
                                                                                      "sections sixteen colgrid"})
                                    for sixteen_colgrid in sixteen_colgrids:
                                        section = sixteen_colgrid.findAll("div", {"class:", split_string})
                                        for section_info_containers_list in section:
                                            section_info_containers = section_info_containers_list.findAll("div", {"class:", "section-info-container"})
                                            numbers = []
                                            for section_info_container in section_info_containers:
                                                data_rows = section_info_container.findAll("div", {"class:", "row"})
                                                for data_row in data_rows:
                                                    six_cols = data_row.findAll("div", {"class:", "seats-info-group six columns"})
                                                    for six_col in six_cols:
                                                        data_div = six_col.find("div")
                                                        for seats_info in data_div.findAll("span", "seats-info"):
                                                            total_seats = seats_info.findAll("span", {"class:", "total-seats"})
                                                            for seat_count in total_seats:
                                                                total_seats_count = seat_count.findAll("span", {"class:", "total-seats-count"})
                                                                for count in total_seats_count:
                                                                    number = int(count.contents[0])
                                                                    numbers.append(number)
                                                            open_seats = seats_info.findAll("span", {"class:", "open-seats"})
                                                            for seat_count in open_seats:
                                                                open_seats_count = seat_count.findAll("span", {"class:", "open-seats-count"})
                                                                for count in open_seats_count:
                                                                    number = int(count.contents[0])
                                                                    numbers.append(number)
                                                            waitlist_seats = seats_info.findAll("span", {"class:", "waitlist"})
                                                            for seat_count in waitlist_seats:
                                                                waitlist_seats_count = seat_count.findAll("a")
                                                                for link_contents in waitlist_seats_count:
                                                                    for count in link_contents.findAll("span", {"class:", "waitlist-count"}):
                                                                        number = int(count.contents[0])
                                                                        numbers.append(number)
                                            section_info_times = section_info_containers_list.findAll("div", {"class:", "class-days-container"})
                                            time = None
                                            time_day = None
                                            time_start = None
                                            time_end = None
                                            for section_info_time in section_info_times:
                                                data_rows = section_info_time.findAll("div", {"class:", "row"})
                                                for data_row in data_rows:
                                                    data_info = data_row.findAll("div", {"class:", "section-day-time-group push_two five columns"})
                                                    for meeting_time in data_info:
                                                        days = meeting_time.findAll("span", {"class:",
                                                                                            "section-days"})
                                                        for day in days:
                                                            time_day = day.contents[0]

                                                        starts = meeting_time.findAll("span", {"class:",
                                                                                            "class-start-time"})
                                                        for start in starts:
                                                            time_start = start.contents[0]

                                                        ends = meeting_time.findAll("span", {"class:",
                                                                                            "class-end-time"})
                                                        for end in ends:
                                                            time_end = end.contents[0]
                                                        if time_day and time_start and time_end:
                                                            time = (time_day, time_start, time_end)
                                                        else:
                                                            time = "No listed time"
                                            time = str(time)
                                            dt[course_id][time] = numbers[0]
                                            course_capcities.append((course_id, time, numbers))
    return dt, course_capcities



in_person_string = "section delivery-f2f"
online_string = "section delivery-online"

c = 1
all_data = {"online": {}, "in person": {}}
online_capacities = []
in_person_capacities = []
for dept in umd_departments:
    all_data["online"][dept], online_capacity = get_count(get_online(dept), online_string)
    online_capacities.append(online_capacity)

    all_data["in person"][dept], in_person_capacity = get_count(get_in_person(dept), in_person_string)
    in_person_capacities.append(in_person_capacity)

    print("Parsed " + dept + " (" + str(c) + "/" + str(len(umd_departments)) + ")")
    c+=1

# pp.pprint(all_data)

online_data = all_data["online"]
in_person_data = all_data["in person"]

count = 0
online_count = 0
in_person_count = 0
for dept in online_data:
    print("Dept:", dept, "has", len(online_data[dept]), "online, and", len(in_person_data[dept]), "in person")
    in_person_count += len(in_person_data[dept])
    online_count += len(online_data[dept])
    count += len(online_data[dept]) + len(in_person_data[dept])
print("There are " + str(count) + " total classes")
print(str(online_count) + " of them are online.")
print(str(in_person_count) + " of them are in person.")


with open('output/course_slots.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quotechar='|')
    writer.writerow(["course type", "course code", "time", "total", "open", "waitlist"])
    for course in online_capacities:
        for tup in course:
            writer.writerow(["online", tup[0], tup[1], tup[2][0], tup[2][1], tup[2][2]])
    for course in in_person_capacities:
        for tup in course:
            writer.writerow(["in person", tup[0], tup[1], tup[2][0], tup[2][1], tup[2][2]])


with open("output/class_info.json", "w") as df:
    json.dump(all_data, df, indent=4, sort_keys=True)


#Total course sections online: [837, 0, 0]
#Total course sections in person: [6332, 0, 0]
