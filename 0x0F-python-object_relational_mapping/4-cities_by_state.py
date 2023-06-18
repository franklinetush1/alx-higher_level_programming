#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb
if __name__ == '__main__':
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT cities.id, cities.name, states.name FROM cities, states \
                     WHERE states.id = state_id ORDER BY cities.id ASC")
    state = mycursor.fetchall()
    for item in state:
        print(item)
