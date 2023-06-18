#!/usr/bin/python3
"""that takes in an argument and displays all values that match arg"""
import sys
import MySQLdb
if __name__ == '__main__':
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE name=% s", (sys.argv[4],))
    state = mycursor.fetchall()
    for item in state:
        print(item)
