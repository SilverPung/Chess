import csv
fieldnames=['','Time_to_100','Speed_record']

def input_data():
    data=[]      
    with open('cars.csv',mode='w',newline='') as input_file:

        writer=csv.DictWriter(input_file,fieldnames=fieldnames)
        data.append({'Name':input(),'Time_to_100':input(),'Speed_record':input()})
        for given in data:
            writer.writerow(given)