## Resources

**Read or watch**:

*   [How To Create a New User and Grant Permissions in MySQL](/rltoken/1tuxYhEv__bmrwkAicbjpA "How To Create a New User and Grant Permissions in MySQL")
*   [How To Use MySQL GRANT Statement To Grant Privileges To a User](/rltoken/km4VxJIBhjKVfiWEBETk-w "How To Use MySQL GRANT Statement To Grant Privileges To a User")
*   [MySQL constraints](/rltoken/AHI2a6vFyr8h4LeI6xK96w "MySQL constraints")
*   [SQL technique: subqueries](/rltoken/Cw-Ah9PKoqXI2tzMSBWG8g "SQL technique: subqueries")
*   [Basic query operation: the join](/rltoken/ptF4SZ183JdHR8B-4Przog "Basic query operation: the join")
*   [SQL technique: multiple joins and the distinct keyword](/rltoken/Hfm_RzeltFsUTLud-96mhQ "SQL technique: multiple joins and the distinct keyword")
*   [SQL technique: join types](/rltoken/ktRZOgLt7iKdUU0JKfu8vQ "SQL technique: join types")
*   [SQL technique: union and minus](/rltoken/WnHLjf7TqurEVuFdDhg59w "SQL technique: union and minus")
*   [MySQL Cheat Sheet](/rltoken/g8QlxhHt2_WHdIXE-2oYYw "MySQL Cheat Sheet")
*   [The Seven Types of SQL Joins](/rltoken/o6faV44f8S34zW3FiO5Mgg "The Seven Types of SQL Joins")
*   [MySQL Tutorial](/rltoken/T3VjE1yBfwJcd1hDD4tItw "MySQL Tutorial")
*   [SQL Style Guide](/rltoken/0NaQZjOUvQuWy0xGPhTkVw "SQL Style Guide")
*   [MySQL 8.0 SQL Statement Syntax](/rltoken/R5KAnzO4iwYo2LgD3eKL8A "MySQL 8.0 SQL Statement Syntax")

Extra resources around relational database model design:

*   [Design](/rltoken/A81_Vk2TV-f_f5wG0HK6Zw "Design")
*   [Normalization](/rltoken/cwgE_DVy7l3ap6lCVJsPZQ "Normalization")
*   [ER Modeling](/rltoken/1JFNpSloiEAI7aLW2rnyKw "ER Modeling")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/SXrjP8A_no4j3TMHUC4NBw "explain to anyone"), **without the help of Google**:

### General

*   How to create a new MySQL user
*   How to manage privileges for a user to a database or table
*   What’s a `PRIMARY KEY`
*   What’s a `FOREIGN KEY`
*   How to use `NOT NULL` and `UNIQUE` constraints
*   How to retrieve datas from multiple tables in one request
*   What are subqueries
*   What are `JOIN` and `UNION`

## Requirements

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
*   All your files should end with a new line
*   All your SQL queries should have a comment just before (i.e. syntax above)
*   All your files should start by a comment describing the task
*   All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   The length of your files will be tested using `wc`

## Tasks

### 1.

 

Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).
```
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user\_0d\_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user\_0d\_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON \*.\* TO 'user\_0d\_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user\_0d\_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON \*.\* TO \`user\_0d\_1\`@\`localhost\`                                                                                                                             
GRANT APPLICATION\_PASSWORD\_ADMIN,AUDIT...,XA\_RECOVER\_ADMIN ON \*.\* TO \`user\_0d\_1\`@\`localhost\`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user\_0d\_2' on host 'localhost'              
guillaume@ubuntu:~/$
```
  

### 2.

 

Write a script that creates the MySQL server user `user_0d_1`.

*   `user_0d_1` should have all privileges on your MySQL server
*   The `user_0d_1` password should be set to `user_0d_1_pwd`
*   If the user `user_0d_1` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 1-create\_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user\_0d\_1@localhost                                                                                                
GRANT SELECT, INSERT..., DROP ROLE ON \*.\* TO \`user\_0d\_1\`@\`localhost\`                                                                                                                             
GRANT APPLICATION\_PASSWORD\_ADMIN,...,XA\_RECOVER\_ADMIN ON \*.\* TO \`user\_0d\_1\`@\`localhost\`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user\_0d\_2' on host 'localhost'
guillaume@ubuntu:~/$
```
  

### 3.

 

Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

*   `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
*   The `user_0d_2` password should be set to `user_0d_2_pwd`
*   If the database `hbtn_0d_2` already exists, your script should not fail
*   If the user `user_0d_2` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 2-create\_read\_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user\_0d\_1@localhost                                                                                                
GRANT SELECT, ..., DROP ROLE ON \*.\* TO \`user\_0d\_1\`@\`localhost\`                                                                                                                             
GRANT APPLICATION\_PASSWORD\_ADMIN,...,XA\_RECOVER\_ADMIN ON \*.\* TO \`user\_0d\_1\`@\`localhost\`                                        
Grants for user\_0d\_2@localhost                                                                                                
GRANT USAGE ON \*.\* TO \`user\_0d\_2\`@\`localhost\`                                                                                 
GRANT SELECT ON \`hbtn\_0d\_2\`.\* TO \`user\_0d\_2\`@\`localhost\`  
guillaume@ubuntu:~/$
```
  

### 4.

 

Write a script that creates the table `force_name` on your MySQL server.

*   `force_name` description:
    *   `id` INT
    *   `name` VARCHAR(256) can’t be null
*   The database name will be passed as an argument of the `mysql` command
*   If the table `force_name` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 3-force\_name.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO force\_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT \* FROM force\_name;' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO force\_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
guillaume@ubuntu:~/$ echo 'SELECT \* FROM force\_name;' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$
```
  

### 5.

 

Write a script that creates the table `id_not_null` on your MySQL server.

*   `id_not_null` description:
    *   `id` INT with the default value `1`
    *   `name` VARCHAR(256)
*   The database name will be passed as an argument of the `mysql` command
*   If the table `id_not_null` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 4-never\_empty.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO id\_not\_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT \* FROM id\_not\_null;' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO id\_not\_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT \* FROM id\_not\_null;' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
id  name
89  Best School
1   Best
guillaume@ubuntu:~/$
```
  

### 6.

 

Write a script that creates the table `unique_id` on your MySQL server.

*   `unique_id` description:
    *   `id` INT with the default value `1` and must be unique
    *   `name` VARCHAR(256)
*   The database name will be passed as an argument of the `mysql` command
*   If the table `unique_id` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 5-unique\_id.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO unique\_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT \* FROM unique\_id;' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique\_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique\_id.id'
guillaume@ubuntu:~/$ echo 'SELECT \* FROM unique\_id;' | mysql -hlocalhost -uroot -p hbtn\_0d\_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$
```
  

### 7.

 

Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

*   `states` description:
    *   `id` INT unique, auto generated, can’t be null and is a primary key
    *   `name` VARCHAR(256) can’t be null
*   If the database `hbtn_0d_usa` already exists, your script should not fail
*   If the table `states` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT \* FROM states;' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
guillaume@ubuntu:~/$
```
  

### 8.

 

Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

*   `cities` description:
    *   `id` INT unique, auto generated, can’t be null and is a primary key
    *   `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
    *   `name` VARCHAR(256) can’t be null
*   If the database `hbtn_0d_usa` already exists, your script should not fail
*   If the table `cities` already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state\_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT \* FROM cities;' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  state\_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state\_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (\`hbtn\_0d\_usa\`.\`cities\`, CONSTRAINT \`cities\_ibfk\_1\` FOREIGN KEY (\`state\_id\`) REFERENCES \`states\` (\`id\`))
guillaume@ubuntu:~/$ echo 'SELECT \* FROM cities;' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  state\_id    name
1   1   San Francisco
guillaume@ubuntu:~/$
```
  

### 9.

 

Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

*   The `states` table contains only one record where `name` = `California` (but the `id` can be different, as per the example)
*   Results must be sorted in ascending order by `cities.id`
*   You are not allowed to use the `JOIN` keyword
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ echo 'SELECT \* FROM states;' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT \* FROM cities;' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  state\_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 8-cities\_of\_california\_subquery.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  name
1   San Francisco
2   San Jose
guillaume@ubuntu:~/$
```
  

### 10.

 

Write a script that lists all cities contained in the database `hbtn_0d_usa`.

*   Each record should display: `cities.id` - `cities.name` - `states.name`
*   Results must be sorted in ascending order by `cities.id`
*   You can use only one `SELECT` statement
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ echo 'SELECT \* FROM states;' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT \* FROM cities;' | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  state\_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 9-cities\_by\_state\_join.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_usa
Enter password: 
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
guillaume@ubuntu:~/$
```
  

### 11.

 

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

*   Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
*   Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
*   You can use only one `SELECT` statement
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 10-genre\_id\_by\_show.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_tvshows
Enter password: 
title   genre\_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$
```
  

### 12.

 

Import the database dump of `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `10-genre_id_by_show.sql`)

Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

*   Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
*   Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
*   If a show doesn’t have a genre, display `NULL`
*   You can use only one `SELECT` statement
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 11-genre\_id\_all\_shows.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_tvshows
Enter password: 
title   genre\_id
Better Call Saul    NULL
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
Homeland    NULL
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$
```
  

### 13.

 

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `11-genre_id_all_shows.sql`)

Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

*   Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
*   Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
*   You can use only one `SELECT` statement
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 12-no\_genre.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_tvshows
Enter password: 
title   genre\_id
Better Call Saul    NULL
Homeland    NULL
guillaume@ubuntu:~/$
```
  

### 14.

 

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `12-no_genre.sql`)

Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

*   Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`
*   First column must be called `genre`
*   Second column must be called `number_of_shows`
*   Don’t display a genre that doesn’t have any shows linked
*   Results must be sorted in descending order by the number of shows linked
*   You can use only one `SELECT` statement
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 13-count\_shows\_by\_genre.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_tvshows
Enter password: 
genre   number\_of\_shows
Drama   5
Comedy  4
Mystery 2
Crime   2
Suspense    2
Thriller    2
Adventure   1
Fantasy 1
guillaume@ubuntu:~/$
```
  

### 15.

 

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `13-count_shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

*   The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
*   Each record should display: `tv_genres.name`
*   Results must be sorted in ascending order by the genre name
*   You can use only one `SELECT` statement
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 14-my\_genres.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_tvshows
Enter password: 
name
Crime
Drama
Mystery
Suspense
Thriller
guillaume@ubuntu:~/$
```
  

### 16.

 

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `14-my_genres.sql`)

Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

*   The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different)
*   Each record should display: `tv_shows.title`
*   Results must be sorted in ascending order by the show title
*   You can use only one `SELECT` statement
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 15-comedy\_only.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_tvshows
Enter password: 
title
New Girl
Silicon Valley
The Big Bang Theory
The Last Man on Earth
guillaume@ubuntu:~/$
```
  

### 17.

 

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `15-comedy_only.sql`)

Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

*   If a show doesn’t have a genre, display `NULL` in the genre column
*   Each record should display: `tv_shows.title` - `tv_genres.name`
*   Results must be sorted in ascending order by the show title and genre name
*   You can use only one `SELECT` statement
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 16-shows\_by\_genre.sql | mysql -hlocalhost -uroot -p hbtn\_0d\_tvshows
Enter password: 
title   name
Better Call Saul    NULL
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter  Crime
Dexter  Drama
Dexter  Mystery
Dexter  Suspense
Dexter  Thriller
Game of Thrones Adventure
Game of Thrones Drama
Game of Thrones Fantasy
Homeland    NULL
House   Drama
House   Mystery
New Girl    Comedy
Silicon Valley  Comedy
The Big Bang Theory Comedy
The Last Man on Earth   Comedy
The Last Man on Earth   Drama
guillaume@ubuntu:~/$
```
