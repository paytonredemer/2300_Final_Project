#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Database configuration inventory management system
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
        with open('schema.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.executescript(sql_script)
        con.commit()
        con.close()
