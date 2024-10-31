import json
import csv
import types


def filter_fields(dt: dict) -> bool:
    if (dt['phoneNumber'].startswith('+1') or dt['phoneNumber'].startswith('1')) and '4.0 Safari' in dt["userAgent"]:
        return True
    else:
        return False


def read_json(read_file: str) -> types.GeneratorType:
    with (open(read_file, 'r') as file):
        arr: list = json.load(file)
        for i in arr:
            if filter_fields(i):
                yield [i['name'], i['address'].replace('\n', ' '), i['email']]


def write_csv(write_file: str, gener: types.GeneratorType) -> None:
    with open(write_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'address', 'mail'])
        for j in gener:
            writer.writerow(j)


result_generator = read_json('in.json')
write_csv('result.csv', result_generator)

