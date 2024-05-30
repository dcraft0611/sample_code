import tkinter as tk
from tkinter import ttk

def convert(event=None):
    value = entry_value.get()
    base = combo_base.get()

    # Convert the input value to decimal
    if base == 'Decimal':
        decimal_value = int(value)
    elif base == 'Binary':
        decimal_value = int(value, 2)
    elif base == 'Octal':
        decimal_value = int(value, 8)
    elif base == 'Hexadecimal':
        decimal_value = int(value, 16)

    # Convert the decimal value to other bases
    binary_value = bin(decimal_value)[2:]
    octal_value = oct(decimal_value)[2:]
    hexadecimal_value = hex(decimal_value)[2:]

    # Update the labels with the converted values
    label_binary.config(text=binary_value)
    label_octal.config(text=octal_value)
    label_hexadecimal.config(text=hexadecimal_value)

root = tk.Tk()
root.title("Number Conversion Calculator")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_value = ttk.Label(frame, text="Value:")
label_value.grid(row=0, column=0, sticky=tk.W)

entry_value = ttk.Entry(frame)
entry_value.grid(row=0, column=1, padx=5, sticky=tk.W)
entry_value.bind("<Return>", convert)

label_base = ttk.Label(frame, text="Base:")
label_base.grid(row=1, column=0, sticky=tk.W)

combo_base = ttk.Combobox(frame, values=['Decimal', 'Binary', 'Octal', 'Hexadecimal'])
combo_base.grid(row=1, column=1, padx=5, sticky=tk.W)
combo_base.current(0)  # Set default selection to Decimal

button_convert = ttk.Button(frame, text="Convert", command=convert)
button_convert.grid(row=2, column=0, columnspan=2, pady=5)

label_binary = ttk.Label(frame, text="Binary:")
label_binary.grid(row=3, column=0, sticky=tk.W)

label_octal = ttk.Label(frame, text="Octal:")
label_octal.grid(row=4, column=0, sticky=tk.W)

label_hexadecimal = ttk.Label(frame, text="Hexadecimal:")
label_hexadecimal.grid(row=5, column=0, sticky=tk.W)

root.mainloop()
