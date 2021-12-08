mysqld --user=mysql --console --skip-name-resolve --skip-networking=0 &
/usr/sbin/httpd -f /etc/apache2/httpd.conf -DFOREGROUND
