import json
import csv

# load the data from the output.json file, which is made by write_file.py
with open('output/class_info.json') as f:
  data = json.load(f)

# write data to classes.csv
with open('output/classes.csv', 'w', newline='\n') as csvfile:
    count = 0
    writer = csv.writer(csvfile, delimiter='\t', quotechar='|')
    writer.writerow(["course status", "course_dept", "course_id", "course_time", "number_seats"])
    for course_status in data:
        course_statuses = data[course_status]
        for course_dept in course_statuses:
            course_ids = course_statuses[course_dept]
            for course_id in course_ids:
                course_info = course_ids[course_id]
                for course_time in course_info:
                    if "None" not in course_time:
                        writer.writerow([course_status, course_dept, course_id, course_time, course_info[course_time]])
                        count += 1
print("Wrote", count, "rows")