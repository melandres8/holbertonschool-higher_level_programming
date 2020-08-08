#!/usr/bin/python3
""" Wait, do you remember the previous task?
    Did you test "Arizona'; TRUNCATE TABLE states ;
    SELECT * FROM states WHERE name = '" as an input? """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], db=argv[3], charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name=%s", (argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()
