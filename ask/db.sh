sudo /etc/init.d/mysql restart
mysql -uroot -e "create database mailru_project;"
mysql -uroot -e "CREATE USER 'ivan'@'localhost' IDENTIFIED BY '1';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON mailru_project.* TO 'ivan'@'localhost' IDENTIFIED BY '1';"
