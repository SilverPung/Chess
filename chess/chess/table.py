import tkinter as tk

class TableInput:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.entries = []

        self.create_table()

    def create_table(self):
        for i in range(self.rows):
            row_entries = []
            for j in range(self.columns):
                entry = tk.Entry(self.root, width=10)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def get_table_values(self):
        table_data = []
        for i in range(self.rows):
            row_data = []
            for j in range(self.columns):
                value = self.entries[i][j].get()
                row_data.append(value)
            table_data.append(row_data)
        return table_data

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Table Input Example")

    # Create a TableInput instance with 3 rows and 4 columns
    table_input = TableInput(root, rows=3, columns=4)

    def on_submit():
        # Get the values from the table and print them
        table_values = table_input.get_table_values()
        print("Table Values:")
        for row in table_values:
            print(row)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=table_input.rows, columnspan=table_input.columns, pady=10)

    root.mainloop()