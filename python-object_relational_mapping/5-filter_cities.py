#!/usr/bin/python3
"""
Prend le nom d'un état comme argument et
liste toutes les villes de cet état, en utilisant la bdd hbtn_0e_4_usa

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    state_name = argv[4]
    cursor.execute("""
                   SELECT cities.name
                   FROM cities
                   INNER JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC
                   """, (state_name,))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
