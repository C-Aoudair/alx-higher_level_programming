#!/usr/bin/python3
"""  lists all states with name maechs a user input from db hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db_connect.cursor()
    cursor.execute(f"""SELECT * FROM states
                   WHERE name = '{sys.argv[4]}' ORDER BY id;""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connect.close()
