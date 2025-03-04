#!/usr/bin/python3
"""
Prend un argument et affiche toutes les valeurs dans la table des états
de hbtn_0e_0_usa où le nom correspond à l'argument.

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4]
                                                                        ))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
