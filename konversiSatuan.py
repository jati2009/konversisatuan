import tkinter as tk
from tkinter import messagebox

# Fungsi konversi suhu
def convert_temperature():
    try:
        temperature = float(entry_temp.get())
        if temp_var.get() == "Celsius to Fahrenheit":
            result = (temperature * 9/5) + 32
        elif temp_var.get() == "Fahrenheit to Celsius":
            result = (temperature - 32) * 5/9
        else:
            result = temperature
        label_result.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Fungsi konversi berat
def convert_weight():
    try:
        weight = float(entry_weight.get())
        if weight_var.get() == "Kilograms to Pounds":
            result = weight * 2.20462
        elif weight_var.get() == "Pounds to Kilograms":
            result = weight * 0.453592
        else:
            result = weight
        label_result.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Fungsi konversi panjang
def convert_length():
    try:
        length = float(entry_length.get())
        if length_var.get() == "Meters to Yards":
            result = length * 1.09361
        elif length_var.get() == "Yards to Meters":
            result = length * 0.9144
        else:
            result = length
        label_result.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Konversi Unit Satuan - Tugas Coding")
root.geometry("600x550")
root.configure(bg="#333333")
root.resizable(False, False)

label_title = tk.Label(root, text="Konversi Unit Satuan", fg="white", bg="#333333")
label_title.pack(pady=10)

frame_temp = tk.Frame(root, bg="#333333")
frame_temp.pack(pady=10)

label_temp = tk.Label(frame_temp, text="Temperature:", fg="white", bg="#333333")
label_temp.grid(row=0, column=0)

temp_var = tk.StringVar()
temp_options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Same"]
temp_var.set(temp_options[0])

temp_menu = tk.OptionMenu(frame_temp, temp_var, *temp_options)
temp_menu.grid(row=0, column=1)

entry_temp = tk.Entry(frame_temp)
entry_temp.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

btn_temp = tk.Button(frame_temp, text="Convert", command=convert_temperature)
btn_temp.grid(row=2, column=0, columnspan=2, pady=5)

frame_weight = tk.Frame(root, bg="#333333")
frame_weight.pack(pady=10)

label_weight = tk.Label(frame_weight, text="Weight:", fg="white", bg="#333333")
label_weight.grid(row=0, column=0)

weight_var = tk.StringVar()
weight_options = ["Kilograms to Pounds", "Pounds to Kilograms", "Same"]
weight_var.set(weight_options[0])

weight_menu = tk.OptionMenu(frame_weight, weight_var, *weight_options)
weight_menu.grid(row=0, column=1)

entry_weight = tk.Entry(frame_weight)
entry_weight.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

btn_weight = tk.Button(frame_weight, text="Convert", command=convert_weight)
btn_weight.grid(row=2, column=0, columnspan=2, pady=5)

frame_length = tk.Frame(root, bg="#333333")
frame_length.pack(pady=10)

label_length = tk.Label(frame_length, text="Length:", fg="white", bg="#333333")
label_length.grid(row=0, column=0)

length_var = tk.StringVar()
length_options = ["Meters to Yards", "Yards to Meters", "Same"]
length_var.set(length_options[0])

length_menu = tk.OptionMenu(frame_length, length_var, *length_options)
length_menu.grid(row=0, column=1)

entry_length = tk.Entry(frame_length)
entry_length.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

btn_length = tk.Button(frame_length, text="Convert", command=convert_length)
btn_length.grid(row=2, column=0, columnspan=2, pady=5)

label_result = tk.Label(root, text="Result: ", fg="white", bg="#333333")
label_result.pack(pady=10)

root.mainloop()
