#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Inventory management system
"""

import tkinter as tk
from tkinter import StringVar, ttk
from db import get_table_column_names, query_db

def update_type(*args):
    type = clicked.get()

    if type == "Charger":
        id_label.config(text="Charger_ID")
        int_label.config(text="Power")
        varchar_label.config(text="Input")
        varchar2_entry.grid_remove()
        output_entry.grid()
        output_label.config(text="Output")
    elif type == "Storage":
        id_label.config(text="Storage_ID")
        int_label.config(text="Storage_Size")
        varchar_label.config(text="Connector")
        output_entry.grid_remove()
        varchar2_entry.grid(row=1, column=5)
        output_label.config(text="Medium")
    elif type == "Cable":
        id_label.config(text="Cable_ID")
        int_label.config(text="Length")
        varchar_label.config(text="Color")
        varchar2_entry.grid_remove()
        output_entry.grid()
        output_label.config(text="Connector")
    update_Treeview(type)

def update_Treeview(table: str):
    column_names = get_table_column_names(table)

    data_result['columns'] = tuple(column_names)

    for column in column_names:
        data_result.heading(column, text=column)

    data_result.delete(*data_result.get_children())
    count = 0
    for record in query_db(table):
        data_result.insert(parent='', index='end', iid=str(count), values=record)
        count += 1

def search_db():
    type = clicked.get()
    # query = f"SELECT * FROM {type}"
    attributes = {}

    if id_entry.get() != "":
        attributes[type+"_ID"] = id_entry.get()
    if brand_entry.get() != "":
        attributes["Brand"] = brand_entry.get()
    if address_entry.get() != "":
        attributes["Address"] = address_entry.get()
    if bin_entry.get() != "":
        attributes["Bin_no"] = bin_entry.get()

    if type == "Charger":
        if int_entry.get() != "":
            attributes["Power"] = int_entry.get()
        if varchar_entry.get() != "":
            attributes["Input"] = varchar_entry.get()
        # add output_entry
    elif type == "Storage":
        if int_entry.get() != "":
            attributes["Storage_Size"] = int_entry.get()
        if varchar_entry.get() != "":
            attributes["Connector"] = varchar_entry.get()
        if varchar2_entry.get() != "":
            attributes["Medium"] = varchar2_entry.get()
    elif type == "Cable":
        if int_entry.get() != "":
            attributes["Length"] = int_entry.get()
        if varchar_entry.get() != "":
            attributes["Color"] = varchar_entry.get()
        # add output_entry


root = tk.Tk()
root.title("Electronic management")

frame = tk.Frame(root)
frame.pack()

# frames
input_frame = tk.LabelFrame(frame, text="Search")
input_frame.grid(row=0, column=0, padx=10,pady=10)

data_frame = tk.LabelFrame(frame, text="Result")
data_frame.grid(row=1,column=0, sticky="news", padx=10,pady=10)

modify_frame = tk.LabelFrame(frame, text="Modify")
modify_frame.grid(row=2,column=0, sticky="news", padx=10,pady=10)

add_frame = tk.LabelFrame(frame, text="Add")
add_frame.grid(row=3,column=0, sticky="news", padx=10,pady=10)

# input section
type_label = tk.Label(input_frame, text= "Electronic Type")
type_label.grid(row=0, column=0)

options = ["Charger", "Storage", "Cable"]
clicked = StringVar()
clicked.set(options[0])
clicked.trace('w', update_type)

type_entry = tk.OptionMenu(input_frame, clicked, *options)
type_entry.grid(row=1, column=0)

id_label = tk.Label(input_frame, text= "Charger_ID")
id_entry = tk.Entry(input_frame)
id_label.grid(row=0, column=1)
id_entry.grid(row=1, column=1)

brand_label = tk.Label(input_frame, text= "Brand")
brand_entry = tk.Entry(input_frame)
brand_label.grid(row=0, column=2)
brand_entry.grid(row=1, column=2)

int_label = tk.Label(input_frame, text= "Power")
int_entry = tk.Entry(input_frame)
int_label.grid(row=0, column=3)
int_entry.grid(row=1, column=3)

varchar_label = tk.Label(input_frame, text= "Input")
varchar_entry = tk.Entry(input_frame)
varchar_label.grid(row=0, column=4)
varchar_entry.grid(row=1, column=4)

# TODO: Add multi select option
output_label = tk.Label(input_frame, text= "Output")
output_entry = tk.Listbox(input_frame)
output_label.grid(row=0, column=5)
output_entry.grid(row=1, column=5)

output_entry.insert(1, "test1")
output_entry.insert(2, "test2")

varchar2_entry = tk.Entry(input_frame)

address_label = tk.Label(input_frame, text= "Address")
address_entry = tk.Entry(input_frame)
address_label.grid(row=0, column=6)
address_entry.grid(row=1, column=6)

bin_label = tk.Label(input_frame, text= "Bin Number")
bin_entry = tk.Entry(input_frame)
bin_label.grid(row=0, column=7)
bin_entry.grid(row=1, column=7)

submit_buttton = tk.Button(input_frame, text= "Search", command=search_db)
submit_buttton.grid(row=1, column=8)


# sql result section
data_result = ttk.Treeview(data_frame)
data_result['columns'] = ("ID", "Brand", "Address")
data_result['show'] = 'headings' # remove default empty column from Treeview

update_Treeview("Charger")

data_result.pack(expand=True, fill='both')


# Edit/change
id_edit_label = tk.Label(modify_frame, text= "ID:")
id_edit_entry = tk.Entry(modify_frame)
id_edit_label.grid(row=0,column=0)
id_edit_entry.grid(row=0,column=1)

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
for widget in input_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in modify_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in add_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

varchar2_entry.grid_remove()
root.mainloop()
