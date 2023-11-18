#!/usr/bin/python3
"""a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db_connect = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=database, charset="utf8")
    mycursor = db_connect.cursor()

    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(state)
    mycursor.execute(sql)

    result = mycursor.fetchall()

    for city in result:
        print(city)
    mycursor.close()
    db_connect.close()
