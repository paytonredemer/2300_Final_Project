#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Inventory management system
"""

import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox
from typing_extensions import IntVar
from db import create_db, get_table_column_names, insert_db, modify_db, query_db
import time
from datetime import datetime

def login(*args) -> None:
    """
    Checks to see if user information is in database.
    If it's in the db, the view is switched.
    Else an error popup is displayed.
    """
    username = username_entry.get()
    query = f"SELECT * FROM User WHERE ID = '{username}' AND Password = '{password_entry.get()}'"
    if len(query_db(query)) > 0:
        current_user.config(text=f"Current user:  {username}")
        update_items_checked_out()
        raise_frame(frame_main)
    else:
        # Throw popup if no user info found
        messagebox.showerror("Invalid login information", f"Login for '{username}' not found or password incorrect")

def logout(*args) -> None:
    """
    Logs user out and brings them back to the login screen
    """
    username_entry.delete(0, "end")
    password_entry.delete(0, "end")
    raise_frame(frame_login)

def add_user(*args) -> None:
    """
    Adds new user to database
    """
    username = add_username_entry.get()
    password = add_password_entry.get()
    name = add_name_entry.get()
    phone = add_phone_entry.get()

    # Insert NULL in db instead of ""
    if name == "":
        name = "NULL"
    else:
        name = f"'{name}'"

    if phone == "":
        phone = "NULL"
    else:
        try:
            phone = int(phone)
        except:
            messagebox.showerror("Invalid phone#", "Integer is required")
            return


    query = f"SELECT * FROM User WHERE ID = '{username}'"
    if len(query_db(query)) > 0:
        # Throw popup if there is already something with that username
        messagebox.showerror("Invalid username", f"'{username}' already taken")
    elif username == "":
        messagebox.showerror("Invalid username", "Username cannot be empty")
    elif password == "":
        messagebox.showerror("Invalid password", "Password cannot be empty")
    else:
        query = f"INSERT INTO User VALUES('{username}', '{password}', {name}, {phone})"
        modify_db(query)
        messagebox.showinfo("User added", f"An account for {username} has been added")
        add_username_entry.delete(0, "end")
        add_password_entry.delete(0, "end")
        add_name_entry.delete(0, "end")
        add_phone_entry.delete(0, "end")
        raise_frame(frame_login)

def update_type(*args):
    type = electronic_type.get()

    if type == "Charger":
        id_label.config(text="Charger_ID")
        int_label.config(text="Power")
        varchar_label.config(text="Input")
        varchar2_entry.grid_remove()
        output_entry.grid()
        output_label.config(text="Output")
        update_output_entry()
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
        update_output_entry()
    update_data_result()

def update_output_entry(*args) -> None:
    """
    Update output options based on current type
    """
    type = electronic_type.get()
    output = ""
    connector = ""
    global connectors
    connectors = {}

    if type == "Charger":
        output = "Output"
        connector = "Type"
    elif type == "Cable":
        output = "Connector"
        connector = "End"
    elif type == "Storage":
        return

    query = f"SELECT DISTINCT {connector} FROM {output}"
    connector_values = query_db(query)
    Menu = tk.Menu(output_entry, tearoff=0)
    for connector in connector_values:
        connectors[connector[0]] = tk.IntVar()
        Menu.add_checkbutton(label = connector[0], variable=connectors[connector[0]])
    output_entry["menu"] = Menu

def update_data_result(*args) -> None:
    """
    Updates data_result based on type
    """
    type = electronic_type.get()
    output = ""
    column_names = get_table_column_names(type)

    if type == "Charger":
        output = "Output"
        column_names.insert(1, output)
    elif type == "Cable":
        output = "Connector"
        column_names.insert(1, output)
    column_names.insert(1, "Checked out")


    data_result['columns'] = tuple(column_names)

    for column in column_names:
        data_result.heading(column, text=column)

    data_result.delete(*data_result.get_children())

    query = f"SELECT * FROM {type}"
    count = 0
    for record in query_db(query):
        values = list(record)
        if len(query_db(f"SELECT * FROM {type}_checkout WHERE {type}_ID = {record[0]}")) > 0:
            values.insert(1, "Yes")
        else:
            values.insert(1, "No")

        if type != "Storage":
            query = f"SELECT * FROM {output} WHERE {type}_ID = {record[0]}"
            outputs = []
            [outputs.append(i[2]) for i in query_db(f"SELECT * FROM {output} WHERE {type}_ID = {record[0]}") ]
            values.insert(2, ", ".join(outputs))

        data_result.insert(parent='', index='end', iid=str(count), values=values)
        count += 1

def search_db(*args) -> None:
    """
    Updates data_result based on input_frame and type
    """
    type = electronic_type.get()
    attributes = {}
    # outputs = [] 
    output = ""

    if type == "Charger":
        output = "Output"
    elif type == "Cable":
        output = "Connector"

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

    # add multi values
    # if type != "Storage":
    #     if bool(connectors):
    #         for output, selected in connectors.items():
    #             print(output, selected)
    #             if selected:
    #                 outputs.append(output)
    #         attributes[output_label.cget("text")] = outputs

    if not attributes:
        query = f"SELECT * FROM {type}"
    else:
        query = f"SELECT * FROM {type} WHERE ("
        for column, value in attributes.items():
            query = query + f"{column} = '{value}' AND "
        query = query[:-5] + ")"

    data_result.delete(*data_result.get_children())

    count = 0
    for record in query_db(query):
        values = list(record)
        if len(query_db(f"SELECT * FROM {type}_checkout WHERE {type}_ID = {record[0]}")) > 0:
            values.insert(1, "Yes")
        else:
            values.insert(1, "No")

        if type != "Storage":
            query = f"SELECT * FROM {output} WHERE {type}_ID = {record[0]}"
            outputs = []
            [outputs.append(i[2]) for i in query_db(f"SELECT * FROM {output} WHERE {type}_ID = {record[0]}") ]
            values.insert(2, ", ".join(outputs))

        data_result.insert(parent='', index='end', iid=str(count), values=values)
        count += 1

def checkout_item(*args):
    """
    Checks out item.
    Checks if item is not checked out and exists in the database before
    """
    type = electronic_type.get()
    id = id_edit_entry.get()
    user_id = username_entry.get()

    # Check if item is checked out
    checkout = query_db(f"SELECT User_ID FROM {type}_checkout WHERE {type}_ID = '{id}'")
    if len(checkout) > 0:
        name = query_db(f"SELECT Name FROM USER WHERE ID = '{checkout[0][0]}'")
        messagebox.showerror("Can't checkout. Item is checked out", f"{name[0][0]} currently has this item checked out")
        return

    # Check if item is in database
    checkout = query_db(f"SELECT {type}_ID FROM {type} WHERE {type}_ID = '{id}'")
    if len(checkout) > 0:
        query = f"INSERT INTO {type}_checkout VALUES({id}, '{user_id}', {int(time.time())})"
        modify_db(query)
        update_items_checked_out()
        messagebox.showinfo("Item checked out", f"{type}# {id} checked out")
    else:
        messagebox.showerror("ID not in database", "Can not find item in database")

def checkin_item(*args):
    """
    Checks in item
    """
    type = electronic_type.get()
    id = id_edit_entry.get()
    user_id = username_entry.get()

    # Check if item is checked out
    checkout = query_db(f"SELECT User_ID FROM {type}_checkout WHERE {type}_ID = '{id}' AND User_ID = '{user_id}'")
    if len(checkout) > 0:
        name = query_db(f"SELECT Name FROM USER WHERE ID = '{checkout[0][0]}'")
        query = f"DELETE FROM {type}_checkout WHERE {type}_ID = '{id}' AND User_ID = '{user_id}'" 
        modify_db(query)
        update_items_checked_out()
        messagebox.showinfo("Item checked in", f"{type}# {id} checked in")
    else:
        messagebox.showerror("ID not checked out", "Item is not checked out or doesn't exist")


def remove_item(*args):
    """
    Removes item from respective table using its ID.
    Checks to make item is in db and not checked out.
    """
    type = electronic_type.get()
    id = id_edit_entry.get()

    # Check if item is checked out
    checkout = query_db(f"SELECT User_ID FROM {type}_checkout WHERE {type}_ID = '{id}'")
    if len(checkout) > 0:
        name = query_db(f"SELECT Name FROM USER WHERE ID = '{checkout[0][0]}'")
        messagebox.showerror("Can't remove. Item is checked out", f"{name[0][0]} currently has this item checked out")
        return

    # Check if item is in database
    checkout = query_db(f"SELECT {type}_ID FROM {type} WHERE {type}_ID = '{id}'")
    if len(checkout) > 0:
        query = f"DELETE FROM {type} WHERE {type}_ID = '{id}'"
        modify_db(query)
        update_data_result()
        messagebox.showinfo("Item removed", f"{id} removed from {type} table")
    else:
        messagebox.showerror("ID not in database", "Can not find item in database")

def add_item(*args):
    pass

def update_items_checked_out(*args) -> None:
    """
    Updates list of user's checked out items to reflect what's in the database
    """
    user_id = username_entry.get()
    query = f"""
    SELECT "Charger" as Type, Charger_ID, Checkout_date FROM Charger_checkout WHERE User_ID = '{user_id}'
    UNION
    SELECT "Storage" as Type, Storage_ID, Checkout_date FROM Storage_checkout WHERE User_ID = '{user_id}'
    UNION
    SELECT "Cable" as Type, Cable_ID, Checkout_date FROM Cable_checkout WHERE User_ID = '{user_id}'
    """
    result = query_db(query)

    items_checked_out.delete(*items_checked_out.get_children())
    count = 0
    for record in result:
        values = (record[0], record[1], datetime.utcfromtimestamp(record[2]).strftime('%Y-%m-%d %I:%M %p'))
        items_checked_out.insert(parent='', index='end', iid=str(count), values=values)
        count += 1

def raise_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Electronic management")

# main screens
frame_main = tk.Frame(root)

frame_login = tk.Frame(root)

frame_add_item = tk.Frame(root)

frame_edit_item = tk.Frame(root)

frame_add_user = tk.Frame(root)

for frame in (frame_main, frame_login, frame_add_user):
    frame.grid(row=0, column=0, sticky="news")

# main frames
user_frame = tk.LabelFrame(frame_main, text= "")
user_frame.grid(row=0, column=0, sticky="nes", padx=10,pady=10)

input_frame = tk.LabelFrame(frame_main, text="Search")
input_frame.grid(row=1, column=0,sticky="s", padx=10,pady=10)

data_frame = tk.LabelFrame(frame_main, text="Result")
data_frame.grid(row=2,column=0, sticky="news", padx=10,pady=10)

modify_frame = tk.LabelFrame(frame_main, text="Modify")
modify_frame.grid(row=3,column=0, sticky="news", padx=10,pady=10)

add_frame = tk.LabelFrame(frame_main, text="Add")
add_frame.grid(row=4,column=0, sticky="news", padx=10,pady=10)

checked_out = tk.LabelFrame(frame_main, text="Items Checked out")
checked_out.grid(row=5,column=0, sticky="news", padx=10,pady=10)

# main screen

# user info section
current_user = tk.Label(user_frame, text= "Current user:")
logout_button = tk.Button(user_frame, text= "Logout", command=logout)
current_user.grid(row=0, column=0,padx=10,pady=5)
logout_button.grid(row=0, column=1,padx=10,pady=5)

# input section
type_label = tk.Label(input_frame, text= "Electronic Type")
type_label.grid(row=0, column=0)

options = ["Charger", "Storage", "Cable"]
electronic_type = StringVar()
electronic_type.set(options[0])
electronic_type.trace('w', update_type)

type_entry = tk.OptionMenu(input_frame, electronic_type, *options)
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

output_label = tk.Label(input_frame, text= "Output")
output_entry = tk.Menubutton(input_frame, text= "Select")
update_output_entry()
connectors = {}

output_label.grid(row=0, column=5)
output_entry.grid(row=1, column=5)

varchar2_entry = tk.Entry(input_frame) # used for Cable

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
update_data_result()

data_result.pack(expand=True, fill='both')


# Edit/change section
id_edit_label = tk.Label(modify_frame, text= "ID:")
id_edit_entry = tk.Entry(modify_frame)
id_edit_label.grid(row=0,column=0)
id_edit_entry.grid(row=0,column=1)

checkout_buttton = tk.Button(modify_frame, text= "Checkout", command=checkout_item)
checkout_buttton.grid(row=0, column=2)

checkin_buttton = tk.Button(modify_frame, text= "Checkin", command=checkin_item)
checkin_buttton.grid(row=0, column=3)

edit_buttton = tk.Button(modify_frame, text= "Edit")
edit_buttton.grid(row=0, column=4)

remove_buttton = tk.Button(modify_frame, text= "Remove", command=remove_item)
remove_buttton.grid(row=0, column=5)


# Add new item section
new_item_label = tk.Label(add_frame, text= "Have a new item?")
new_item_button = tk.Button(add_frame, text= "Add", command=lambda:raise_frame(frame_add_user)) # TODO: Update to move frame to seperate add interface rather than add user
new_item_label.grid(row=1,column=0)
new_item_button.grid(row=1, column=1)

# Checked out items section
items_checked_out = ttk.Treeview(checked_out)
checked_out_columns = ("Type", "Item ID", "Checkout date")
items_checked_out['columns'] = checked_out_columns
for column in checked_out_columns:
    items_checked_out.heading(column, text=column)
items_checked_out['show'] = 'headings' # remove default empty column from Treeview
items_checked_out.pack(expand=True, fill='both')

# Login screen

login_labelframe = tk.LabelFrame(frame_login, text="Login")
login_labelframe.place(in_=frame_login, anchor="center", relx=.5, rely=.5)

username_label = tk.Label(login_labelframe, text= "Username:")
username_entry = tk.Entry(login_labelframe)
username_label.grid(row=0,column=0)
username_entry.grid(row=0,column=1)

password_label = tk.Label(login_labelframe, text= "Password:")
password_entry = tk.Entry(login_labelframe)
password_label.grid(row=1,column=0)
password_entry.grid(row=1,column=1)

login_button = tk.Button(login_labelframe, text='Login', command=login)
login_button.grid(row=1, column=2)

create_user_labelframe = tk.LabelFrame(frame_login, text="")
create_user_labelframe.place(in_=frame_login, anchor="n", relx=.5, rely=.6)

create_user_label = tk.Label(create_user_labelframe, text= "Need account?")
create_user_button = tk.Button(create_user_labelframe, text='Create account', command=lambda:raise_frame(frame_add_user))
create_user_label.grid(row=0,column=0)
create_user_button.grid(row=0,column=1)

# Add user screen
add_user_labelframe = tk.LabelFrame(frame_add_user, text="Add user")
add_user_labelframe.place(in_=frame_add_user, anchor="center", relx=.5, rely=.5)

add_username_label = tk.Label(add_user_labelframe, text= "Username:")
add_username_entry = tk.Entry(add_user_labelframe)
add_username_label.grid(row=0,column=0)
add_username_entry.grid(row=0,column=1)

add_password_label = tk.Label(add_user_labelframe, text= "Password:")
add_password_entry = tk.Entry(add_user_labelframe)
add_password_label.grid(row=1,column=0)
add_password_entry.grid(row=1,column=1)

add_name_label = tk.Label(add_user_labelframe, text= "Name:")
add_name_entry = tk.Entry(add_user_labelframe)
add_name_label.grid(row=2,column=0)
add_name_entry.grid(row=2,column=1)

add_phone_label = tk.Label(add_user_labelframe, text= "Phone#:")
add_phone_entry = tk.Entry(add_user_labelframe)
add_phone_label.grid(row=3,column=0)
add_phone_entry.grid(row=3,column=1)

add_user_button = tk.Button(add_user_labelframe, text='Add user', command=add_user)
add_user_button.grid(row=4, column=2)

add_user_back_button = tk.Button(add_user_labelframe, text='Back to Login', command=logout)
add_user_back_button.grid(row=4, column=0)

# Add item screen here

# Modify item screen here

# visual stuff
for widget in input_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in modify_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in add_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in login_labelframe.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in create_user_labelframe.winfo_children():
    widget.grid_configure(padx=10,pady=5)

for widget in add_user_labelframe.winfo_children():
    widget.grid_configure(padx=10,pady=5)

varchar2_entry.grid_remove()
raise_frame(frame_login)
root.mainloop()
