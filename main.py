import pandas as pd
import csv
import ast
import rich


def search_replace():

    # Definér filsti og de strenge, der skal findes/erstattes
    file_path = 'leon.csv'
    search_text1 = r"\/"
    search_text2 = "/"
    replace_text1 = "-"
    replace_text2 = "-"

    # 1. Læs filens indhold
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # 2. Erstat teksten
    #data = data.replace(search_text1, replace_text1)
    data = data.replace(search_text2, replace_text2)

    # 3. Skriv det opdaterede indhold tilbage
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)


def google():
    import csv
    import json

    file_path = 'leon.csv'

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, quotechar='"', doublequote=True)
        next(reader, None)  # Spring overskriften over

        for row in reader:
            # Hent 6. kolonne (index 5)
            raw_string = row[5]

            try:
                # Konvertér JSON-streng til Python dict
                my_dict = json.loads(raw_string)
                #print(f"Hentet værdi: {my_dict.get('ClientIP')}")
                creation_time = my_dict.get('CreationTime')
                client_ip = my_dict.get('ClientIP')
                operation = my_dict.get('Operation')
                userkey = my_dict.get('UserKey')
                usertype = my_dict.get('UserType')
                workload = my_dict.get('Workload')
                userid = my_dict.get('UserId')
                is_managed_device = my_dict.get('IsManagedDevice')
                item_type = my_dict.get('ItemType')

                if client_ip != '46.16.17.54':
                    if client_ip != '46.16.17.55':
                        if client_ip != None:
                            print(f"Time: {creation_time} || ClientIP: {client_ip} || Operation: {operation} || UserKey: {userkey} || Workload: {workload} || UserId: {userid} || IsManagedDevice: {is_managed_device} || ItemType: {item_type}")

            except json.JSONDecodeError:
                # Håndter rækker med ugyldigt format eller tomme felter
                print(f"Fejl i format: {raw_string}")

    #for key in my_dict:
    #    print(key)


def main():
    dicts_list = []

    with open('leon.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists

        for row in reader:
            # Extract 5th column (index 4) and convert to dict
            dict_obj = ast.literal_eval(row[5])
            dicts_list.append(dict_obj)

    for row in dicts_list:
        # Now dicts_list contains a dictionary for every row
        print(row)



google()
#search_replace()
#main()