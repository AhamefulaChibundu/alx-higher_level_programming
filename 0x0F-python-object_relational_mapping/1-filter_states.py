#!/usr/bin/python3
""" This script lists all states with a name starting with N
from the database hbtn_0e_0_usa """
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
    SELECT id, name
    FROM states
    WHERE name LIKE BINARY'N%'
    ORDER BY id ASC""")
    rows = mycur.fetchall()
    for row in rows:
        print(row)
