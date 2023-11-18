#!/usr/bin/python3
"""This is a script that filters states
listing those that start with the letter N"""

import MySQLdb
import sys
if __name__ == '__main__':

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_connect = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=database, charset="utf8")
    cur = db_connect.cursor()

    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(sql)

    result = cur.fetchall()

    for city in result:
        print(city)
    cur.close()
    db_connect.close()
