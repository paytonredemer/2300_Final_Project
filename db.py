#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Database configuration help functions for the inventory management system
"""

import os
import sqlite3

path = "inventory.db"


def create_db() -> None:
    """
    Checks to see if a sqlite database is present in directory. If not, creates
    database and populates it.
    """
    if not os.path.isfile(path):
        with open('database.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.executescript(sql_script)
        con.commit()
        con.close()

def get_table_column_names(table: str) -> list[str]:
    """
    Returns list of table column names
    """
    con = sqlite3.connect(path)
    cur = con.cursor()
    res = cur.execute("SELECT name FROM PRAGMA_TABLE_INFO(?)", (table,))
    result = res.fetchall()
    con.close()

    # return list of strings instead of list of single tuples
    return [x[0] for x in result]


def query_db(query) -> list[tuple]:
    """
    Run queries that don't modify the database
    """
    con = sqlite3.connect(path)
    cur = con.cursor()
    res = cur.execute(query)
    query = res.fetchall()
    con.close()

    return query

def modify_db(query: str) -> None:
    """
    Run queries that do modify the database
    """
    con = sqlite3.connect(path)
    cur = con.cursor()
    con.execute("PRAGMA foreign_keys = ON")
    cur.execute(query)
    con.commit()
    con.close()

def add_item(item: str, attributes: tuple, multivalue: list[tuple] = []) -> None:
    """
    Add entries into database
    """
    con = sqlite3.connect(path)
    cur = con.cursor()

    if item == "Charger":
        add_charger((con,cur), attributes, multivalue)
    elif item == "Storage":
        add_storage((con,cur), attributes)
    elif item == "Cable":
        add_cable((con,cur), attributes, multivalue)
    else:
        print("Invalid item")

    con.close()


def add_charger(database: tuple[sqlite3.Connection, sqlite3.Cursor], attributes: tuple, outputs: list[tuple]) -> None:
    database[1].execute("INSERT INTO Charger VALUES(?, ?, ?, ?, ?, ?)", attributes)
    database[0].commit()

    database[1].executemany("INSERT INTO Output VALUES(?, ?,?)", outputs)
    database[0].commit()

def add_storage(database: tuple[sqlite3.Connection, sqlite3.Cursor], attributes: tuple) -> None:
    database[1].execute("INSERT INTO Cable VALUES(?, ?, ?, ?, ?, ?, ?)", attributes)
    database[0].commit()


def add_cable(database: tuple[sqlite3.Connection, sqlite3.Cursor], attributes: tuple, connectors: list[tuple]) -> None:
    database[1].execute("INSERT INTO Cable VALUES(?, ?, ?, ?, ?, ?)", attributes)
    database[0].commit()

    database[1].executemany("INSERT INTO Connector VALUES(?, ?,?)", connectors)
    database[0].commit()

create_db()
