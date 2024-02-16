#!/usr/bin/python3
"""this module for exicuting sql command via MySQLdb modeule."""
import MySQLdb
import sys

args = sys.argv

db_connection = MySQLdb.connect("localhost", args[1], args[2], args[3])
cursor = db_connection.cursor()
table = f"{sys.argv[3]}.states"

cursor.execute(f"SELECT * FROM {table} WHERE name LIKE 'N%';")
rows = cursor.fetchall()
for row in rows:
    print(f"{row}")

db_connection.close()
