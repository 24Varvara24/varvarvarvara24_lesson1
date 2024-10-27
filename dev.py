import json, csv

result = None

with (open('in.json', 'r') as file):
    arr = json.load(file)
    result = ([i['name'], i['address'], i['email']] for i in arr if
              (i['phoneNumber'].startswith('+1') or i['phoneNumber'].startswith('1')) and '4.0 Safari' in i[
                  "userAgent"])

with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    for j in result:
        writer.writerow(j)
