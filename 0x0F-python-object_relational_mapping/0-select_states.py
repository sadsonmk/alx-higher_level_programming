#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db_connect = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=database)

    cur = db_connect.cursor()
    sql = f"SELECT * FROM states ORDER BY id"
    cur.execute(sql)

    result = cur.fetchall()

    for state in result:
        print(state)
