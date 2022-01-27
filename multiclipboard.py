import sys
import clipboard
import json

from itsdangerous import exc

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    # Opens file (where filepath is the location)
    # in write mode (If file exists: overwrites it. If file doesn't exist: creates one)
    # and stores it in variable f
    with open(filepath, "w") as f:
        json.dump(data, f)  # Saves data in var f in the JSON file


def load_data(filepath):
    try:
        # The following line would result to an error if the JSON file didn't yet exists, hence try / except
        with open(filepath, "r") as f:  # Reads the JSON file
            data = json.load(f)
            return data  # Returns JSON data as Python dictionary
    except:
        return {}  # If JSON file doesn't yet exist, returns an empty dictionary


# argv is a variable that contains the arguments passed to a program through the command line
# The length needs to be 2 since the first item in argv is the name of the python file,
# and the second one is the actual command.
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)  # Loads a Python dictionary with the data

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key does not exist.")

    elif command == "list":
        print(data)  # Prints all key-value pairs on the multiclipboard
    else:
        print("Unknown command")
else:
    print("Please pass only one command.")
