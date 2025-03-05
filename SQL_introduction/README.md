## Resources

**Read or watch**:

*   [What is Database & SQL?](/rltoken/jRAhwW4u4YvZtLtMGU2_6g "What is Database & SQL?")
*   [Install MySQL (MySQL Server)](/rltoken/s3m_emsaSthyY041Wacgxg "Install MySQL (MySQL Server)")
*   [A Basic MySQL Tutorial](/rltoken/m_0RMf4RcC5NrHyjY1xN3w "A Basic MySQL Tutorial")
*   [Basic SQL statements: DDL and DML](/rltoken/4Y8WpsRDXWjgWRqTas_ZxA "Basic SQL statements: DDL and DML") (_no need to read the chapter “Privileges”_)
*   [Basic queries: SQL and RA](/rltoken/0G5umqVQe5ltlrcZbq1WxA "Basic queries: SQL and RA")
*   [SQL technique: functions](/rltoken/LSKIFzHPwoub-dcFi9cf0A "SQL technique: functions")
*   [SQL technique: subqueries](/rltoken/FAho4oM2b4uER5SvWK9Pwg "SQL technique: subqueries")
*   [What makes the big difference between a backtick and an apostrophe?](/rltoken/QEr3XcBPhIR-E8NSSn1nzg "What makes the big difference between a backtick and an apostrophe?")
*   [MySQL Cheat Sheet](/rltoken/DGejihlnOkkNq-qJFM15MA "MySQL Cheat Sheet")
*   [MySQL 8.0 SQL Statement Syntax](/rltoken/ePNUeloWxfiXwec7HeKe7Q "MySQL 8.0 SQL Statement Syntax")
*   Duo to a temporary bug to some of the resources aboves, you can find most of the information [here](/rltoken/sxuxGmSk-ZEwuVa1AKKoVQ "here")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/6bUOgrGi5Yd_I65Jp9bAfg "explain to anyone"), **without the help of Google**:

### General

*   What’s a database
*   What’s a relational database
*   What does SQL stand for
*   What’s MySQL
*   How to create a database in MySQL
*   What does `DDL` and `DML` stand for
*   How to `CREATE` or `ALTER` a table
*   How to `SELECT` data from a table
*   How to `INSERT`, `UPDATE` or `DELETE` data
*   What are `subqueries`
*   How to use MySQL functions

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

 

Write a script that lists all databases of your MySQL server.
```
guillaume@ubuntu:~/$ cat 0-list\_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
information\_schema                                                                           
mysql                                                                                        
performance\_schema                                                                           
sys        
guillaume@ubuntu:~/$
```
  

### 2.

 

Write a script that creates the database `hbtn_0c_0` in your MySQL server.

*   If the database `hbtn_0c_0` already exists, your script should not fail
*   You are not allowed to use the `SELECT` or `SHOW` statements
```
guillaume@ubuntu:~/$ cat 1-create\_database\_if\_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list\_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information\_schema
hbtn\_0c\_0
mysql
performance\_schema
guillaume@ubuntu:~/$ cat 1-create\_database\_if\_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$
```
  

### 3.

 

Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

*   If the database `hbtn_0c_0` doesn’t exist, your script should not fail
*   You are not allowed to use the `SELECT` or `SHOW` statements
```
guillaume@ubuntu:~/$ cat 0-list\_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn\_0c\_0                                                                                    
information\_schema                                                                           
mysql                                                                                        
performance\_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove\_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list\_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information\_schema                                                                           
mysql                                                                                        
performance\_schema                                                                           
sys        
guillaume@ubuntu:~/$
```
  

### 4.

 

Write a script that lists all the tables of a database in your MySQL server.

*   The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)
```
guillaume@ubuntu:~/$ cat 3-list\_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables\_in\_mysql                                                                              
columns\_priv                                                                                 
component                                                                                    
db                                                                                           
default\_roles                                                                                
engine\_cost                                                                                  
func                                                                                         
general\_log                                                                                  
global\_grants                                                                                
gtid\_executed                                                                                
help\_category                                                                                
help\_keyword                                                                                 
help\_relation                                                                                
help\_topic                                                                                   
innodb\_index\_stats                                                                           
innodb\_table\_stats                                                                           
password\_history                                                                             
plugin                                                                                       
procs\_priv                                                                                   
proxies\_priv                                                                                 
replication\_asynchronous\_connection\_failover                                                 
replication\_asynchronous\_connection\_failover\_managed                                         
role\_edges                                                                                   
server\_cost                                                                                  
servers                                                                                      
slave\_master\_info                                                                            
slave\_relay\_log\_info                                                                         
slave\_worker\_info                                                                            
slow\_log                                                                                     
tables\_priv                                                                                  
time\_zone                                                                                    
time\_zone\_leap\_second                                                                        
time\_zone\_name                                                                               
time\_zone\_transition                                                                         
time\_zone\_transition\_type                                                                    
user
guillaume@ubuntu:~/$
```
  

### 5.

 

Write a script that creates a table called `first_table` in the current database in your MySQL server.

*   `first_table` description:
    *   `id` INT
    *   `name` VARCHAR(256)
*   The database name will be passed as an argument of the `mysql` command
*   If the table `first_table` already exists, your script should not fail
*   You are not allowed to use the `SELECT` or `SHOW` statements
```
guillaume@ubuntu:~/$ cat 4-first\_table.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list\_tables.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
Tables\_in\_hbtn\_0c\_0
first\_table
guillaume@ubuntu:~/$
```
  

### 6.

 

Write a script that prints the following description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

*   The database name will be passed as an argument of the `mysql` command
*   You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements
```
guillaume@ubuntu:~/$ cat 5-full\_table.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
Table   Create Table                                                                         
first\_table     CREATE TABLE \`first\_table\` (\\n  \`id\` int DEFAULT NULL,\\n  \`name\` varchar(256) DEFAULT NULL\\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci        
guillaume@ubuntu:~/$
```
  

### 7.

 

Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

*   All fields should be printed
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 6-list\_values.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
guillaume@ubuntu:~/$
```
  

### 8.

 

Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

*   New row:
    *   `id` = `89`
    *   `name` = `Best School`
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 7-insert\_value.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list\_values.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert\_value.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert\_value.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list\_values.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$
```
  

### 9.

 

Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 8-count\_89.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$
```
  

### 10.

 

Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

*   `second_table` description:
    *   `id` INT
    *   `name` VARCHAR(256)
    *   `score` INT
*   The database name will be passed as an argument to the `mysql` command
*   If the table `second_table` already exists, your script should not fail
*   You are not allowed to use the `SELECT` and `SHOW` statements
*   Your script should create these records:
    *   `id` = 1, `name` = “John”, `score` = 10
    *   `id` = 2, `name` = “Alex”, `score` = 3
    *   `id` = 3, `name` = “Bob”, `score` = 14
    *   `id` = 4, `name` = “George”, `score` = 8
```
guillaume@ubuntu:~/$ cat 9-full\_creation.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
guillaume@ubuntu:~/$
```
  

### 11.

 

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

*   Results should display both the score and the name (in this order)
*   Records should be ordered by score (top first)
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 10-top\_score.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$
```
  

### 12.

 

Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

*   Results should display both the score and the name (in this order)
*   Records should be ordered by score (top first)
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 11-best\_score.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$
```
  

### 13.

 

Write a script that updates the score of Bob to `10` in the table `second_table`.

*   You are not allowed to use Bob’s id value, only the `name` field
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 12-no\_cheating.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top\_score.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$
```
  

### 14.

 

Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 13-change\_class.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top\_score.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$
```
  

### 15.

 

Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

*   The result column name should be `average`
*   The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$
```
  

### 16.

 

Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

*   The result should display:
    *   the `score`
    *   the number of records for this `score` with the label `number`
*   The list should be sorted by the number of records (descending)
*   The database name will be passed as an argument to the `mysql` command
```
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$
```
  

### 17.

 

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

*   Don’t list rows where the `name` column does not contain a value
*   Results should display the score and the name (in this order)
*   Records should be listed by descending score
*   The database name will be passed as an argument to the `mysql` command

In this example, new data have been added to the table `second_table`.
```
guillaume@ubuntu:~/$ cat 16-no\_link.sql | mysql -hlocalhost -uroot -p hbtn\_0c\_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$
```
