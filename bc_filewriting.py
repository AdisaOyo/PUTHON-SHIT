'''
Python writing files (.txt, .json, .csv)
'''
import csv
import json

txt_data = "I like pizza"
file_path = "BRO CODE/output.txt"
# I am setting them to keyword arguments with the file and mode variales

with open(file = file_path, mode = "w") as file: # 'w' to write file if it exists and 'x' if it does not exist if it exists we will recieve an error 'a' is for append and 'r' is for read
    file.write(txt_data)
    print(f"Text file {file_path} was created")
    # w will overwrite a file
#first append
with open(file = file_path, mode = "a") as file:
    file.write(" " + txt_data)
    print(f"Text file {file_path} was appended")
#second append
with open(file = file_path, mode = "a") as file:
    file.write("\n" + txt_data + "\n")
    print(f"Text file {file_path} was appended")

try:
    with open(file = file_path, mode = "x") as file:
        file.write(txt_data)
        print(f"Text file {file_path} was created")
except FileExistsError:
    print("That file already exists")

employees = ["SPongebob", "Eugeine", "Squidward", "Patrick"]

try:
    with open(file = file_path, mode = "a") as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"Text file {file_path} added to")
except FileExistsError:
    print("That file already exists")

# a json file is filled with key:value pairs

dic_employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}
new_file_path = "BRO CODE/json.json" # i need to import json module if i want to use it
try:
    with open(file = new_file_path, mode = "w") as file:
        json.dump(dic_employee, file, indent=4)
        print(f"json file '{new_file_path}' was created")
except FileExistsError:
    print("That file already exists")
# need to import csv module csv file is used to store stuff like excel sheets
datastruct_employees = [["Name", "Age", "Job"],
                        ["Spongebob", 30, "Cook"],
                        ["Squidward", 45, "Cashier"],
                        ["Patrick", 27, "Janitor"]
                        ]
csv_file_path = "BRO CODE/csv.csv" 
#                                                        newline =   # is used to remove new lines from the file when writing
try:
    with open(file = csv_file_path, mode = "w", newline="") as file: 
        writer = csv.writer(file) # writer is an object
        for row in datastruct_employees:
            writer.writerow(row)
        print(f"csv {csv_file_path} added to")
except FileExistsError:
    print("That file already exists")

# if i do not iterate over all the rows it will not give output