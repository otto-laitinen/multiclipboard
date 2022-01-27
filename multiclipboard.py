import sys
import clipboard
import json


def save_items(filepath, data):
    # Opens a file (where filepath is the location)
    # in write mode (If file exists: overwrites it. If file doesn't exist: creates one)
    # and stores it in variable f
    with open(filepath, "w") as f:
        json.dump(data, f)  # Saves data in var f in the JSON file


def load_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data


# argv is a variable that contains the arguments passed to a program through the command line.
# The length needs to be 2 since the first item in argv is the name of the python file,
# and the second one is the actual command.
if len(sys.argv) == 2:
    command = sys.argv[1]

    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("Please pass only one command.")
