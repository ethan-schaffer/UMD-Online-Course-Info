import json

# load the data from the output.json file, which is made by write_file.py
with open('output/class_info.json') as f:
  data = json.load(f)

with open('output/class_info.js', 'w', newline='\n') as file:
    dt = json.dumps(data, indent=4, sort_keys=True)
    file.write("const class_info = " +dt + ";")
