import csv

people = {}

with open('names.csv', 'r') as file:

    csv_file = csv.reader(file)

    next(csv_file)

    for line in csv_file:
        # print(line)
        people[line[0]] = {'last_name' : line[1], 'email' : line[2]}
    
print(people)

        
