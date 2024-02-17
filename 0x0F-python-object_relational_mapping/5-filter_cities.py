#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db_connect.cursor()
    cursor.execute("""SELECT name FROM cities
                   WHERE state_id = (SELECT id from states
                   WHERE name = %s);""", (sys.argv[4], ))
    print(", ".join([city[0] for city in cursor.fetchall()]))
    cursor.close()
    db_connect.close()
