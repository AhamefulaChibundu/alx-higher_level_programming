#!/usr/bin/python3
""" This script lists all cities from the database hbtn_0e_4_usa """
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
    mycur.execute(
        """
        SELECT id,
        name,
        (SELECT name FROM states WHERE state_id=id)
        FROM cities ORDER BY id
        """
    )
    rows = mycur.fetchall()
    for row in rows:
        print(row)
