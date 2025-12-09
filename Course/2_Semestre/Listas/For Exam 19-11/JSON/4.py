import json
with open('status_report.json', 'r') as file:
    done = json.load(file)
    print(done)