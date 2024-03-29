#!/usr/bin/python3
""" This script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    mycur = mydb.cursor()
    mycur.execute("""
    SELECT *
    FROM states
    WHERE name
    LIKE BINARY '{}'
    ORDER BY id""".format(sys.argv[4]))
    rows = mycur.fetchall()
    for row in rows:
        print(row)
