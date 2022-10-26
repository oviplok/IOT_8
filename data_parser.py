import json


def parse_json(_json_filename):
    with open(_json_filename) as file:
        data = json.load(file)

    for i, _message in enumerate(data, 1):
        print(f"Message {i}:")
        for _measure in _message.keys():
            print(f"\t{_measure}: {_message[_measure]}")

