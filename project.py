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

user_info_frame = tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=10,pady=10)

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

address_label = tk.Label(user_info_frame, text= "Address")
address_entry = tk.Entry(user_info_frame)
address_label.grid(row=0, column=4)
address_entry.grid(row=1, column=4)

bin_label = tk.Label(user_info_frame, text= "Bin Number")
bin_entry = tk.Entry(user_info_frame)
bin_label.grid(row=0, column=5)
bin_entry.grid(row=1, column=5)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

root.mainloop()
