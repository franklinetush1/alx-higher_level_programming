#!/usr/bin/python3
"""lists all states with a name starting with N"""
import sys
import MySQLdb
if __name__ == '__main__':
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE name \
                     LIKE 'N%' ORDER BY id ASC")
    state = mycursor.fetchall()
    for item in state:
        print(item)
