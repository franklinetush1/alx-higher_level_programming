#!/usr/bin/python3
"""takes a state as an argument and lists all cities of that state"""
import sys
import MySQLdb

if __name__ == '__main__':
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = mydb.cursor()
    state_name = sys.argv[4]
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id WHERE \
            states.name = %s ORDER BY cities.id ASC;"
    mycursor.execute(query, (state_name,))
    state = mycursor.fetchall()
    for item in state:
        print(", ".join([item]))
