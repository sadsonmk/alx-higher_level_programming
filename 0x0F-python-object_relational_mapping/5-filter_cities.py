#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db_connect = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=database, charset='utf8')
    mycursor = db_connect.cursor()
    sql = f"""SELECT cities.name FROM cities JOIN
          states ON cities.state_id=states.id WHERE states.name='{state}'"""

    mycursor.execute(sql)
    results = mycursor.fetchall()

    cities = []
    for city in results:
        cities.append(city)
    my_city = ', '.join(city[0] for city in cities)
    print(my_city)
    mycursor.close()
    db_connect.close()
