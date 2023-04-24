#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Inventory management system
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Electronic management")
tab_control = ttk.Notebook(root)

charger_tab = ttk.Frame(tab_control)
storage_tab = ttk.Frame(tab_control)
cable_tab = ttk.Frame(tab_control)
all_tab = ttk.Frame(tab_control)

tab_control.add(charger_tab, text = "Charger")
tab_control.add(storage_tab, text = "Storage")
tab_control.add(cable_tab, text = "Cable")
tab_control.add(all_tab, text = "All")
tab_control.pack(expand= 1, fill = "both")

# col1 = tk.Label(text="Col 1")
# col1.grid(column=0, row=0)
#
# col2 = tk.Label(text="Col 2")
# col2.grid(column=1, row=0)
# greeting.pack()

root.mainloop()
