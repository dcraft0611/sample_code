import tkinter as tk
from tkinter import ttk

def convert():
    decimal_value = entry_decimal.get()

    # Convert decimal to binary, octal, and hexadecimal
    binary_value = bin(int(decimal_value))[2:]
    octal_value = oct(int(decimal_value))[2:]
    hexadecimal_value = hex(int(decimal_value))[2:]

    # Update the labels with the converted values
    label_binary.config(text="Binary:" + binary_value)
    label_octal.config(text=octal_value)
    label_hexadecimal.config(text=hexadecimal_value)

root = tk.Tk()
root.title("Number Conversion Calculator")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_decimal = ttk.Label(frame, text="Decimal:")
label_decimal.grid(row=0, column=0, sticky=tk.W)

entry_decimal = ttk.Entry(frame)
entry_decimal.grid(row=0, column=1, padx=5, sticky=tk.W)

button_convert = ttk.Button(frame, text="Convert", command=convert)
button_convert.grid(row=0, column=2, padx=5, sticky=tk.W)

label_binary = ttk.Label(frame, text="Binary:")
label_binary.grid(row=1, column=0, sticky=tk.W)

label_octal = ttk.Label(frame, text="Octal:")
label_octal.grid(row=2, column=0, sticky=tk.W)

label_hexadecimal = ttk.Label(frame, text="Hexadecimal:")
label_hexadecimal.grid(row=3, column=0, sticky=tk.W)

root.mainloop()
