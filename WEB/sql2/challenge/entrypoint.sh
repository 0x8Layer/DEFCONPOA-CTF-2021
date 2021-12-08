#!/bin/ash

# Secure entrypoint
chmod 600 /entrypoint.sh

rm /var/www/localhost/htdocs/index.html
mkdir /var/www/localhost/htdocs/chall
mv /var/www/localhost/htdocs/* /var/www/localhost/htdocs/chall

# Initialize & Start MariaDB
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld
mysql_install_db --user=mysql --ldata=/var/lib/mysql
mysqld --user=mysql --console --skip-name-resolve --skip-networking=0 &

# Wait for mysql to start
while ! mysqladmin ping -h'localhost' --silent; do echo "not up" && sleep .2; done


mysql -u root << EOF
SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
CREATE DATABASE sql2;

CREATE TABLE sql2.user (
    login VARCHAR(10), 
    pass VARCHAR(51)
);

INSERT INTO sql2.user (login, pass) VALUES ('admin', 'js&bWjv_iDs@b%#V_ncHj-s1&ncO');

ALTER USER 'root'@'localhost' IDENTIFIED BY 'mYSq1_p@@s_bUg_9273';
FLUSH PRIVILEGES;
EOF


# Start cron deamon
crond -f &

/usr/bin/supervisord -c /etc/supervisord.conf
