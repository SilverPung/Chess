import csv
fieldnames=['Name','Time_to_100','Speed_record']
def input_data():
    data=[]
    with open('cars.csv',mode='r',newline='') as output_file:
        reader=csv.DictReader(output_file,fieldnames=fieldnames,delimiter=',')
        for row in reader:
            data.append(row)        
    with open('cars.csv',mode='w',newline='') as input_file:

        writer=csv.DictWriter(input_file,fieldnames=fieldnames)
        data.append({'Name':input(),'Time_to_100':input(),'Speed_record':input()})
        for given in data:
            writer.writerow(given)

def print_data():
    with open('cars.csv',mode='r',newline='') as output_file:
        reader=csv.DictReader(output_file,fieldnames=fieldnames,delimiter=',')
        for row in reader:
            print(row)  


if __name__=='__main__':
    print_data()