#!/usr/bin/python3
""" script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
and writes one that is safe from MySQL injections! """
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
    WHERE name LIKE %s
    ORDER BY id""", (sys.argv[4], ))
    rows = mycur.fetchall()
    for row in rows:
        print(row)
