import csv

try:

    '''
    with open('names.csv', 'r') as file:

        csv_file = csv.reader(file)           # Read the CSV File

        # next(csv_file)                      # Iterate to the Next Line

        # for line in csv_file:
        #     print(line[2])
        
        ## Copying Content of one file to another
        with open('new_names.csv', 'w') as n_file:
            csv_wr = csv.writer(n_file, delimiter = '\t')  # Write to the CSV File

            for line in csv_file:
                csv_wr.writerow(line)
    '''

    ## Opening Files specifying Delimeters
    '''
    with open('new_names.csv', 'r') as file:
        csv_file = csv.reader(file, delimiter = '\t')
        
        for line in csv_file:
            print(line)
    '''

    ## Storing off the Names in Dictionary Directly
    with open('names.csv', 'r') as file:

        csv_file = csv.DictReader(file)
        
        # for line in csv_file:
        #    print(line)

        with open('new_names_dict.csv', 'w') as n_file:

            field_names = ['first_name', 'last_name']                                      # Note - Not Keeping off Email Field
            csv_wr = csv.DictWriter(n_file, fieldnames = field_names, delimiter = '\t')

            csv_wr.writeheader()

            for line in csv_file:
                del line['email']
                csv_wr.writerow(line)

except FileNotFoundError:
    print("File Doesn't Exist!")

