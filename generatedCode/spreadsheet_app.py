import tkinter as tk
from tkinter import ttk

class SpreadsheetApp:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.entries = []

        # Create a frame to hold the spreadsheet
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Create the spreadsheet grid of entry widgets
        for i in range(rows):
            row_entries = []
            for j in range(columns):
                entry = ttk.Entry(self.frame, width=10)
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Add a button to print the current state of the spreadsheet
        self.button_print = ttk.Button(root, text="Print Spreadsheet", command=self.print_spreadsheet)
        self.button_print.pack(pady=5)

    def print_spreadsheet(self):
        print("Current Spreadsheet State:")
        for i, row in enumerate(self.entries):
            row_data = [entry.get() for entry in row]
            print(f"Row {i+1}: {row_data}")

# Create the Tkinter root window
root = tk.Tk()
root.title("Spreadsheet App")

# Create an instance of the SpreadsheetApp class with 5 rows and 3 columns
spreadsheet_app = SpreadsheetApp(root, rows=5, columns=3)

# Run the Tkinter event loop
root.mainloop()
