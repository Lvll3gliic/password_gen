This app will generate secure passwords
Mysql database and mariadb server 
- sudo apt install mariadb-server
- sudi mysql_secure_installation

root parole :

lvll3gliic@Edgars:~/password_gen$ sudo mysql -u root -p 
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 57
Server version: 10.3.31-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE passwords CHARACTER SET utf8;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> CREATE USER 'password_gen' IDENTIFIED BY '';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> flush privileges;
Query OK, 0 rows affected (0.000 sec)

MariaDB [(none)]> quit
Bye
