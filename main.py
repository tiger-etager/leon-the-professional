import pandas as pd
import csv
import ast
from os import name

import rich


list_of_dicts = []


def main():

    df = pd.read_csv('bogholderi.csv')

    # Convert the string representation of dictionaries into actual dict objects
    # Replace 'your_column_name' with the actual name of your column
    #df['AuditData'] = df['AuditData'].apply(ast.literal_eval)
    dictionaries = df.iloc[:, 5].apply(ast.literal_eval).tolist()

    # Now you can access specific keys or store them in a variable
    #first_row_dict = df['AuditData'][0]
    #print(first_row_dict['ClientIP'])
    print(dictionaries)


def main2():
    dicts_list = []

    with open('bogholderi.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists

        for row in reader:
            # Extract 5th column (index 4) and convert to dict
            dict_obj = ast.literal_eval(row[5])
            dicts_list.append(dict_obj)

    for row in dicts_list:
        # Now dicts_list contains a dictionary for every row
        print(row)





main2()