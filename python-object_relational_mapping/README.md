## Resources

**Read or watch**:

*   [Object-relational mappers](/rltoken/tCytNeWUzuWhAn9APwtp9A "Object-relational mappers")
*   [mysqlclient/MySQLdb documentation](/rltoken/V8KJv3QCReECPZ0V-kXRwg "mysqlclient/MySQLdb documentation") (_please don’t pay attention to `_mysql`_)
*   [MySQLdb tutorial](/rltoken/j_7jU3C9Jsa0o53pgfwxOQ "MySQLdb tutorial")
*   [SQLAlchemy tutorial](/rltoken/7y1s8FDE_0S-uhBtCgt5-A "SQLAlchemy tutorial")
*   [SQLAlchemy](/rltoken/j6kxlUETdjiFwiu0k_JI6Q "SQLAlchemy")
*   [mysqlclient/MySQLdb](/rltoken/vzsiR8tCdY3_OWsMH33jUA "mysqlclient/MySQLdb")
*   [Introduction to SQLAlchemy](/rltoken/7m6F57mBASM7A2r_GcIeMA "Introduction to SQLAlchemy")
*   [Flask SQLAlchemy](/rltoken/riV6WcWo1MGRpF3WSmv4Zw "Flask SQLAlchemy")
*   [10 common stumbling blocks for SQLAlchemy newbies](/rltoken/uRrjdEkHmjrVenCqjwJRWQ "10 common stumbling blocks for SQLAlchemy newbies")
*   [Python SQLAlchemy Cheatsheet](/rltoken/RfLwdV21O_TVoQU4iwaIFw "Python SQLAlchemy Cheatsheet")
*   [SQLAlchemy ORM Tutorial for Python Developers](/rltoken/2BoGpuT2vAaoeuC3SN_wPA "SQLAlchemy ORM Tutorial for Python Developers") (_**Warning:** This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL_)
*   [SQLAlchemy Tutorial](/rltoken/DrwY56jSHCOADKEbSOBa0A "SQLAlchemy Tutorial")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/zAH3PxVw_N-4dQ45aCW8yw "explain to anyone"), **without the help of Google**:

### General

*   How to connect to a MySQL database from a Python script
*   How to `SELECT` rows in a MySQL table from a Python script
*   How to `INSERT` rows in a MySQL table from a Python script
*   What ORM means
*   How to map a Python Class to a MySQL table

## Requirements

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
*   Your files will be executed with `MySQLdb` version `2.0.x`
*   Your files will be executed with `SQLAlchemy` version `1.4.x`
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   You are not allowed to use `execute` with sqlalchemy

## Tasks

### 1.

 

Write a script that lists all `states` from the database `hbtn_0e_0_usa`:

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ cat 0-select\_states.sql
-- Create states table in hbtn\_0e\_0\_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn\_0e\_0\_usa;
USE hbtn\_0e\_0\_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select\_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./0-select\_states.py root root hbtn\_0e\_0\_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 2.

 

Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ cat 0-select\_states.sql
-- Create states table in hbtn\_0e\_0\_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn\_0e\_0\_usa;
USE hbtn\_0e\_0\_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select\_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./1-filter\_states.py root root hbtn\_0e\_0\_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 3.

 

Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

*   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   You must use `format` to create the SQL query with the user input
*   Results must be sorted in ascending order by `states.id`
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ cat 0-select\_states.sql
-- Create states table in hbtn\_0e\_0\_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn\_0e\_0\_usa;
USE hbtn\_0e\_0\_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select\_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./2-my\_filter\_states.py root root hbtn\_0e\_0\_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 4.

 

Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` as an input?
```
guillaume@ubuntu:~/$ ./2-my\_filter\_states.py root root hbtn\_0e\_0\_usa "Arizona'; TRUNCATE TABLE states ; SELECT \* FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/$ ./0-select\_states.py root root hbtn\_0e\_0\_usa
guillaume@ubuntu:~/$
```
What? Empty?

Yes, it’s an [SQL injection](/rltoken/d0bQ5pmhaRPHtf0OJI9-Vg "SQL injection") to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

*   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ cat 0-select\_states.sql
-- Create states table in hbtn\_0e\_0\_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn\_0e\_0\_usa;
USE hbtn\_0e\_0\_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select\_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./3-my\_safe\_filter\_states.py root root hbtn\_0e\_0\_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 5.

 

Write a script that lists all `cities` from the database `hbtn_0e_4_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `cities.id`
*   You can use only `execute()` once
*   Results must be displayed as they are in the example below
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ cat 4-cities\_by\_state.sql
-- Create states table in hbtn\_0e\_4\_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn\_0e\_4\_usa;
USE hbtn\_0e\_4\_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    state\_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state\_id) REFERENCES states(id)
);
INSERT INTO cities (state\_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state\_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state\_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state\_id, name) VALUES (4, "New York");
INSERT INTO cities (state\_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 4-cities\_by\_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./4-cities\_by\_state.py root root hbtn\_0e\_4\_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 6.

 

Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

*   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
*   You must use the module `MySQLdb` (`import MySQLdb`)
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `cities.id`
*   You can use only `execute()` once
*   The results must be displayed as they are in the example below
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ cat 4-cities\_by\_state.sql
-- Create states table in hbtn\_0e\_4\_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn\_0e\_4\_usa;
USE hbtn\_0e\_4\_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    state\_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state\_id) REFERENCES states(id)
);
INSERT INTO cities (state\_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state\_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state\_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state\_id, name) VALUES (4, "New York");
INSERT INTO cities (state\_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ ./5-filter\_cities.py root root hbtn\_0e\_4\_usa Texas

guillaume@ubuntu:~/$ cat 4-cities\_by\_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./5-filter\_cities.py root root hbtn\_0e\_4\_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/$ ./5-filter\_cities.py root root hbtn\_0e\_4\_usa Hawaii

guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 7.

 

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250305%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250305T083639Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=77c8f85ff5333fa8684a803875c5a00bfeac9fb557bf37495414587862786582)

Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

*   `State` class:
    *   inherits from `Base` [Tips](/rltoken/62tIVCmGm735_tJWLxtJrQ "Tips")
    *   links to the MySQL table `states`
    *   class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    *   class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
*   You must use the module `SQLAlchemy`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   **WARNING:** all classes who inherit from `Base` **must** be imported before calling `Base.metadata.create_all(engine)`
```
guillaume@ubuntu:~/$ cat 6-model\_state.sql
-- Create database hbtn\_0e\_6\_usa
CREATE DATABASE IF NOT EXISTS hbtn\_0e\_6\_usa;
USE hbtn\_0e\_6\_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/$ cat 6-model\_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn\_0e\_6\_usa.states' doesn't exist
guillaume@ubuntu:~/$ cat 6-model\_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model\_state import Base, State

from sqlalchemy import (create\_engine)

if \_\_name\_\_ == "\_\_main\_\_":
    engine = create\_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv\[1\], sys.argv\[2\], sys.argv\[3\]), pool\_pre\_ping=True)
    Base.metadata.create\_all(engine)

guillaume@ubuntu:~/$ ./6-model\_state.py root root hbtn\_0e\_6\_usa
guillaume@ubuntu:~/$ cat 6-model\_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE \`states\` (\\n  \`id\` int(11) NOT NULL AUTO\_INCREMENT,\\n  \`name\` varchar(128) NOT NULL,\\n  PRIMARY KEY (\`id\`)\\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 8.

 

Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   The results must be displayed as they are in the example below
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ cat 7-model\_state\_fetch\_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 7-model\_state\_fetch\_all.sql | mysql -uroot -p hbtn\_0e\_6\_usa
Enter password: 
guillaume@ubuntu:~/$ ./7-model\_state\_fetch\_all.py root root hbtn\_0e\_6\_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 9.

 

Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   The state you display must be the first in `states.id`
*   You are not allowed to fetch all states from the database before displaying the result
*   The results must be displayed as they are in the example below
*   If the table `states` is empty, print `Nothing` followed by a new line
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ ./8-model\_state\_fetch\_first.py root root hbtn\_0e\_6\_usa
1: California
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 10.

 

Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `states.id`
*   The results must be displayed as they are in the example below
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ ./9-model\_state\_filter\_a.py root root hbtn\_0e\_6\_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 11.

 

Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

*   Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search` (SQL injection free)
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   You can assume you have one record with the state name to search
*   Results must display the `states.id`
*   If no state has the name you searched for, display `Not found`
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ ./10-model\_state\_my\_get.py root root hbtn\_0e\_6\_usa Texas
3
guillaume@ubuntu:~/$ ./10-model\_state\_my\_get.py root root hbtn\_0e\_6\_usa Illinois
Not found
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 12.

 

Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Print the new `states.id` after creation
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ ./11-model\_state\_insert.py root root hbtn\_0e\_6\_usa 
6
guillaume@ubuntu:~/$ ./7-model\_state\_fetch\_all.py root root hbtn\_0e\_6\_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 13.

 

Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Change the name of the `State` where `id = 2` to `New Mexico`
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ ./12-model\_state\_update\_id\_2.py root root hbtn\_0e\_6\_usa 
guillaume@ubuntu:~/$ ./7-model\_state\_fetch\_all.py root root hbtn\_0e\_6\_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 14.

 

Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ ./13-model\_state\_delete\_a.py root root hbtn\_0e\_6\_usa 
guillaume@ubuntu:~/$ ./7-model\_state\_fetch\_all.py root root hbtn\_0e\_6\_usa 
2: New Mexico
4: New York
guillaume@ubuntu:~/$
```
**No test cases needed**

  

### 15.

 

Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

*   `City` class:
    *   inherits from `Base` (imported from `model_state`)
    *   links to the MySQL table `cities`
    *   class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    *   class attribute `name` that represents a column of a string of 128 characters and can’t be null
    *   class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to `states.id`
*   You must use the module `SQLAlchemy`

Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:

*   Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*   You must use the module `SQLAlchemy`
*   You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*   Your script should connect to a MySQL server running on `localhost` at port `3306`
*   Results must be sorted in ascending order by `cities.id`
*   Results must be display as they are in the example below (`<state name>: (<city id>) <city name>`)
*   Your code should not be executed when imported
```
guillaume@ubuntu:~/$ cat 14-model\_city\_fetch\_by\_state.sql
-- Create database hbtn\_0e\_14\_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn\_0e\_14\_usa;
USE hbtn\_0e\_14\_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO\_INCREMENT, 
    state\_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state\_id) REFERENCES states(id)
);
INSERT INTO cities (state\_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state\_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state\_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state\_id, name) VALUES (4, "New York");
INSERT INTO cities (state\_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 14-model\_city\_fetch\_by\_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./14-model\_city\_fetch\_by\_state.py root root hbtn\_0e\_14\_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/$
```
**No test cases needed**
