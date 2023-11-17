#!/usr/bin/python3
"""This is a script that filters states
listting those that start with the letter N"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_connect = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=database)
    mycursor = db_connect.cursor()

    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
    mycursor.execute(sql)

    result = mycursor.fetchall()

    for state in result:
        print(state)
