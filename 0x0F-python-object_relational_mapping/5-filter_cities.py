#!/usr/bin/python3
"""takes a state as an argument and lists all cities of that state"""
import sys
import MySQLdb
if __name__ == '__main__':
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT cities.id, cities.name, states.name \
                     FROM cities JOIN states ON cities.state_id = states.id \
                     WHERE states.name = '{}';".format(sys.argv[4]))
    state = mycursor.fetchall()
    for item in state:
        print(", ".join([item[1]))
