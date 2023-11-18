#!/usr/bin/python3
"""This is a script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_connect = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=database, charset='utf8')
    cur = db_connect.cursor()
    sql = """SELECT cities.id, cities.name, states.name FROM cities
            JOIN states ON states.id=cities.state_id"""
    cur.execute(sql)

    results = cur.fetchall()

    for city in results:
        print(city)

    cur.close()
    db_connect.close()
