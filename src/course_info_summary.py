import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

# load the data from the output.json file, which is made by write_file.py
with open('output/class_info.json') as f:
  data = json.load(f)

umd_departments = []

with open('dept_codes.txt', 'r') as f:
    for line in f:
        currentPlace = line[:-1] # remove linebreak which is the last character of the string
        umd_departments.append(currentPlace)

def total_courses_by_status(code):
    lst = []
    for course_status in data:
        if data[course_status]:
            val = (course_status, len(data[course_status][code]))
            lst.append(val)
    return lst

def all_courses_by_dept(code):
    lst = []
    for course_status in data:
        if data[course_status]:
            for i in data[course_status][code]:
                lst.append(i)
    return lst

summary_data = {}

with open('output/dept_summary.txt', 'w', newline='\n') as csvfile:
    csvfile.write("code\tin person\tonline\n")
    for dept_code in umd_departments:
        summary_data[dept_code] = total_courses_by_status(dept_code)
        csvfile.write(dept_code + "\t" + str(summary_data[dept_code][0][1]) + "\t" + str(summary_data[dept_code][1][1]) + "\n")

pp.pprint(summary_data)