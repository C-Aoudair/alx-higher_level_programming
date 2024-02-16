#!/usr/bin/python3
"""this module for exicuting sql command via MySQLdb modeule."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
        cursor = db_connection.cursor()

        cursor.execute(f"SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row}")

        db_connection.close()

    except Exception as error:
        pass
