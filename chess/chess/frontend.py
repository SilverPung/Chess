import tkinter as tk
from tkinter import ttk
import subprocess
import ast
from table import TableInput
import csv
new_window=None
input_window=None
class Commands:
    def __init__(self) -> None:
        pass
    
    def add_player(self):
        global window
        window.destroy()

        window = tk.Tk()
        window.title("Get Information Example")

        text = tk.Label(window, text='Podaj Imie')
        text.grid(row=0, column=0, pady=5, padx=5)

        id_entry = tk.Entry(window)
        id_entry.grid(row=0, column=1, pady=5, padx=5)

        text1 = tk.Label(window, text='Podaj Nazwisko')
        text1.grid(row=1, column=0, pady=5, padx=5)

        id1_entry = tk.Entry(window)
        id1_entry.grid(row=1, column=1, pady=5, padx=5)

        get_button = tk.Button(window, text="Dodaj Zawodnika", command=lambda: self.add_it(id_entry, id1_entry))
        get_button.grid(row=2, column=0, columnspan=2, pady=10)

        g_button = tk.Button(window, text="Wylosuj", command=lambda: self.shuffle())
        g_button.grid(row=3, column=0, columnspan=2, pady=10)

        window.mainloop()

    def add_scores(self,):
        pass
    
    def shuffle(self):
        global new_window
        new_window=None
        input_window=None
        global window
        if window:
            window.destroy()
        window = tk.Tk()
        window.title("Get Information Example")
        command = 'python chess\\chess\\main.py --shuffle'
        from_sys_shuffle(command)
        command = 'python chess\\chess\\main.py --print-players'
        from_sys(command)
        self.add_scores()
        
        

    def add_it(self, name, surname):
        command = f'python chess\\chess\\main.py --add-player --name {name.get()} --surname {surname.get()}'
        to_sys(command)
        name.delete(0, tk.END)
        surname.delete(0, tk.END)
        command = 'python chess\\chess\\main.py --print-players'
        from_sys(command)

def from_sys(command):
    result = subprocess.check_output(command, text=True)
    output_label_in_new_window(result)
def from_sys_shuffle(command):
    result = subprocess.check_output(command, text=True)
    output_label(result)
def output_label(result):
    apc=Commands()
    headers = ["Id", "ID_przeciwnika"]
    result = ast.literal_eval(result)
  
    # Destroy the earlier version of the new window
    for col, header in enumerate(headers):
        header_label = tk.Label(window, text=header, relief=tk.RIDGE, width=15)
        header_label.grid(row=0, column=col, pady=5, padx=5)
    input_window=None
    for row, rowData in enumerate(result, start=1):
        for col, value in enumerate(rowData):
            cell_label = tk.Label(window, text=value, relief=tk.RIDGE, width=15)
            cell_label.grid(row=row, column=col, pady=5, padx=5)
    submit_button = tk.Button(window, text="Wpisz dane", command=lambda: save(result))
    submit_button.grid(pady=10,padx=15)
    submit_button = tk.Button(window, text="Losuj", command=lambda: apc.shuffle())
    submit_button.grid(pady=10)
def save(result):

    global input_window  # Keep a reference to the new window
    input_window=None
        # Destroy the earlier version of the new window
    if input_window:
        input_window.destroy()

    input_window = tk.Toplevel()
    input_window.title("Table Example")
    input_window.geometry("+1100+50")
    table_input=TableInput(input_window,len(result),2)
    submit_button = tk.Button(input_window, text="Wpisz dane", command=lambda: on_submit(table_input,result))
    submit_button.grid(row=table_input.rows + 1, columnspan=table_input.columns + 1, pady=10)
def on_submit(table_input,result):
        global input_window
        # Get the values from the table and print them
        table_values = table_input.get_table_values()
        fieldnames=['id','score']
        with open('chess\\scores.csv',mode='w',newline='') as input_file:
            data=[]
            writer=csv.DictWriter(input_file,fieldnames=fieldnames)
            for n in range(0,len(result)):
            
                data.append({'id':result[n][0],'score':table_values[n][0]})
                data.append({'id':result[n][1],'score':table_values[n][1]})
            for given in data:
                writer.writerow(given)
        command = f'python chess\\chess\\main.py --add-round'
        to_sys(command)
        input_window.destroy()


    # Set the geometry to position the window slightly to the left

def to_sys(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            pass
        else:
            print("Command failed with an error code:", result.returncode)
            print("Error Output:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", str(e))

def output_label_in_new_window(result):
    headers = ["Id", "Imie", "Nazwisko","Wynik"]
    result = ast.literal_eval(result)

    global new_window  # Keep a reference to the new window

    # Destroy the earlier version of the new window
    if new_window:
        new_window.destroy()

    new_window = tk.Toplevel()
    new_window.title("Table Example")

    # Set the geometry to position the window slightly to the left
    new_window.geometry("+500+50")  # Adjust the values as needed

    for col, header in enumerate(headers):
        header_label = tk.Label(new_window, text=header, relief=tk.RIDGE, width=15)
        header_label.grid(row=0, column=col, pady=5, padx=5)

    for row, rowData in enumerate(result, start=1):
        for col, value in enumerate(rowData):
            cell_label = tk.Label(new_window, text=value, relief=tk.RIDGE, width=15)
            cell_label.grid(row=row, column=col, pady=5, padx=5)

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Combobox Example")

    selected_value = tk.StringVar()

    combobox = ttk.Combobox(window, textvariable=selected_value)
    combobox['values'] = ("Dodaj zawodnika", "Losuj")
    combobox.grid(row=0, column=0, pady=10, padx=10)

    selection_label = tk.Label(window, textvariable=selected_value)
    selection_label.grid(row=1, column=0, pady=5, padx=10)

    def on_select(event):
        command = selected_value.get()
        apc = Commands()
        match(command):
            case 'Dodaj zawodnika':
                apc.add_player()
            case 'Losuj':
                apc.shuffle()

    combobox.bind("<<ComboboxSelected>>", on_select)

    window.mainloop()