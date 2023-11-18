#!/usr/bin/python3
"""This is a script that takes in arguments and
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument. But this time,
    write one that is safe from MySQL injections!"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db_connect = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=database)
    mycursor = db_connect.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE %s", (state,))

    result = mycursor.fetchall()

    for city in result:
        print(city)
    mycursor.close()
    db_connect.close()
