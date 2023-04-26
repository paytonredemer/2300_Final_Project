#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Inventory management system
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Electronic management")

frame = tk.Frame(root)
frame.pack()

# frames
user_info_frame = tk.LabelFrame(frame, text="Search")
user_info_frame.grid(row=0, column=0, padx=10,pady=10)

data_frame = tk.LabelFrame(frame, text="Result")
data_frame.grid(row=1,column=0, sticky="news", padx=10,pady=10)

modify_frame = tk.LabelFrame(frame, text="Modify")
modify_frame.grid(row=2,column=0, sticky="news", padx=10,pady=10)

add_frame = tk.LabelFrame(frame, text="Add")
add_frame.grid(row=3,column=0, sticky="news", padx=10,pady=10)

# input section
charger_id_label = tk.Label(user_info_frame, text= "Charger_ID")
charger_id_entry = tk.Entry(user_info_frame)
charger_id_label.grid(row=0, column=0)
charger_id_entry.grid(row=1, column=0)

power_label = tk.Label(user_info_frame, text= "Power")
power_entry = tk.Entry(user_info_frame)
power_label.grid(row=0, column=1)
power_entry.grid(row=1, column=1)

brand_label = tk.Label(user_info_frame, text= "Brand")
brand_entry = tk.Entry(user_info_frame)
brand_label.grid(row=0, column=2)
brand_entry.grid(row=1, column=2)

input_label = tk.Label(user_info_frame, text= "Input")
input_entry = tk.Entry(user_info_frame)
input_label.grid(row=0, column=3)
input_entry.grid(row=1, column=3)

# TODO: Add multi select option
# output_label = tk.Label(user_info_frame, text= "Output")
# output_entry = tk.Listbox(user_info_frame)
# output_label.grid(row=0, column=4)
# output_entry.grid(row=1, column=4)
#
# output_entry.insert(1, "test1")
# output_entry.insert(2, "test2")

address_label = tk.Label(user_info_frame, text= "Address")
address_entry = tk.Entry(user_info_frame)
address_label.grid(row=0, column=5)
address_entry.grid(row=1, column=5)

bin_label = tk.Label(user_info_frame, text= "Bin Number")
bin_entry = tk.Entry(user_info_frame)
bin_label.grid(row=0, column=6)
bin_entry.grid(row=1, column=6)

submit_buttton = tk.Button(user_info_frame, text= "Search")
submit_buttton.grid(row=1, column=7)


# sql result section
data_result = ttk.Treeview(data_frame)
data_result.pack(expand=True, fill='both')


# Edit/change
id_label = tk.Label(modify_frame, text= "ID:")
id_entry = tk.Entry(modify_frame)
id_label.grid(row=0,column=0)
id_entry.grid(row=0,column=1)

checkout_buttton = tk.Button(modify_frame, text= "Checkout")
checkout_buttton.grid(row=0, column=2)

edit_buttton = tk.Button(modify_frame, text= "Edit")
edit_buttton.grid(row=0, column=3)

remove_buttton = tk.Button(modify_frame, text= "Remove")
remove_buttton.grid(row=0, column=4)


# Add new item
new_item_label = tk.Label(add_frame, text= "Have a new item?")
new_item_button = tk.Button(add_frame, text= "Add")
new_item_label.grid(row=1,column=0)
new_item_button.grid(row=1, column=1)


# visual stuff
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in modify_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in add_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

root.mainloop()
