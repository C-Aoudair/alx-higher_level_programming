#!/usr/bin/python3
"""  lists all states with name starting with N from database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connect.close()
