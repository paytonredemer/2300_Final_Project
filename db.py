#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Payton Redemer
File: db.py

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
        with open("database.sql", "r") as sql_file:
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


# create database if not present in directory
# called on import
create_db()
