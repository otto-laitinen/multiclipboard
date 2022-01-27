import sys
import clipboard
import json

# argv is a variable that contains the arguments passed to a program through the command line.

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
