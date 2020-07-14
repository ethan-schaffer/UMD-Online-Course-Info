from bs4 import BeautifulSoup
import requests
import pprint
from datetime import datetime
import pytz
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

def get_soup_in_person(dept):
    url = get_in_person(dept)
    data = requests.get(url).content
    soup = BeautifulSoup(data, 'html.parser')
    return soup

def get_soup_online(dept):
    url = get_online(dept)
    data = requests.get(url).content
    soup = BeautifulSoup(data, 'html.parser')
    return soup

def aggregate_components(src, a, b, c):
    components = []
    for i in src.findAll(a, {b: c}):
        components.append(i)
    return components

def parse_section(times, section_mode):
    section_list = []
    for time in times:
        section_number = str(time.find("span", {"class": "section-id"}).contents[0]).strip()
        section_instructor = time.find("span", {"class": "section-instructor"}).contents[0]
        section_total_seats = time.find("span", {"class": "total-seats-count"}).contents[0]
        section_open_seats = time.find("span", {"class": "open-seats-count"}).contents[0]

        section_days = time.findAll("span", {"class": "section-days"})
        section_class_start = time.findAll("span", {"class": "class-start-time"})
        section_class_end = time.findAll("span", {"class": "class-end-time"})

        timeslot = None
        if len(section_days) > 0 and len(section_class_start) > 0 and len(section_class_end) > 0:
            timeslot = section_days[0].contents[0] + " " + section_class_start[0].contents[0] + " " + section_class_end[0].contents[0]

        disc_time = None
        if len(section_days) > 1 and len(section_class_start) > 1 and len(section_class_end) > 1:
            disc_time = section_days[1].contents[0] + " " + section_class_start[1].contents[0] + " " + section_class_end[1].contents[0]

        if "a href" in str(section_instructor):
            section_instructor = section_instructor.contents[0]
        section_instructor = str(section_instructor)

        section_list.append([section_number, section_mode, timeslot, disc_time, section_instructor, section_total_seats, section_open_seats])
    return section_list

def get_by_type(data, type_string):
    full_info = []

    courses = aggregate_components(data, "div", "class", "course")
    for course in courses:
        name = course.find("span", {"class": "course-title"}).contents[0]
        course_id = course.get("id")
        dept = course_id[:4]
        entry = [course_id, dept, name]

        times = aggregate_components(course, "div", "class", type_string)
        section_mode = "online"
        if type_string == "section delivery-f2f":
            section_mode = "in person"
        full = parse_section(times, section_mode)

        if not full == []:
            full_info.append([entry, full])

    return full_info

def get_data(dept):

    out = []
    in_person = get_by_type(get_soup_in_person(dept), "section delivery-f2f")
    online = get_by_type(get_soup_online(dept), "section delivery-online")

    for i in in_person:
        out.append(i)

    for j in online:
        out.append(j)
    return out

dt = []
count = 1
for code in umd_departments:
    print("Parsed " + code + " (" + str(count) + "/" + str(len(umd_departments)) + ")")
    count += 1
    dt += get_data(code)

output = {}

for basic_info, lst in dt:
    if basic_info[0] not in output:
        output[basic_info[0]] = {}
    output[basic_info[0]]["department"] = basic_info[1]
    output[basic_info[0]]["course-name"] = basic_info[2]
    section_info = {}
    for section in lst:
        section_info[section[0]] = {'instructor' : section[4],
                                    'lecture-time' : section[2],
                                    'lab-time' : section[3],
                                    'learning-mode' : section[1],
                                    'capacity' : section[5],
                                    'open-seats' : section[6]}
    output[basic_info[0]]["sections"] = section_info

with open("data_prototypev1.js", "w") as df:
        text = json.dumps(output, indent=4, sort_keys=True)

        tz_NY = pytz.timezone('America/New_York')
        datetime_east_coast = datetime.now(tz_NY)
        current_time = datetime_east_coast.strftime("%H:%M:%S")
        current_date = datetime_east_coast.today().strftime('%Y-%m-%d')

        df.write("let last_updated = '" + current_time + " " + current_date + "';\n\n")
        df.write("let catalog = [\n" + text + "\n];")

with open('output/classes.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quotechar='|')
    writer.writerow(["course status", "course_dept", "course_id", "course_time", "number_seats", "open_seats", "course_name", "instructor", "discussion_time"])
    for basic_info, lst in dt:
        for section in lst:
            writer.writerow([section[1], basic_info[1], basic_info[0], section[2], section[5], section[6], basic_info[2], section[4], section[3]])