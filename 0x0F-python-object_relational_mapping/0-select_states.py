#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb
if __name__ == '__main__':
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY id ASC")
    state = mycursor.fetchall()
    for item in state:
        print(item)
