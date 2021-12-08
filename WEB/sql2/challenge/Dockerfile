FROM alpine:edge

# Setup user
RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

# Setup system packages
RUN apk --no-cache --update \
    add apache2 \
    curl \
    vim \
    openrc \
    php7-apache2 \
    php7-bcmath \
    php7-bz2 \
    php7-calendar \
    php7-common \
    php7-ctype \
    php7-curl \
    php7-dom \
    php7-gd \
    php7-iconv \
    php7-json \
    php7-mbstring \
    php7-mcrypt \
    php7-mysqli \
    php7-mysqlnd \
    php7-openssl \
    php7-pdo_mysql \
    php7-pdo_pgsql \
    php7-pdo_sqlite \
    php7-phar \
    php7-session \
    php7-xml \
    php7-xmlrpc \
    mariadb \
    mariadb-client \
    supervisor \
    && mkdir -p /run/apache2 \
    && ln -sf /dev/stdout /var/log/apache2/access.log \
    && ln -sf /dev/stderr /var/log/apache2/error.log


COPY chall/ /var/www/localhost/htdocs

# Expose the port apache is listening on
EXPOSE 5007 3306

# Populate database and start supervisord
COPY --chown=root entrypoint.sh /entrypoint.sh

RUN sed -i 's@^#LoadModule rewrite_module modules/mod_rewrite\.so@LoadModule rewrite_module modules/mod_rewrite.so@' /etc/apache2/httpd.conf 

RUN sed -i 's/Listen 80/Listen 5007/g' /etc/apache2/httpd.conf

RUN sed -i 's/\/var\/www\/localhost\/htdocs/\/var\/www\/localhost\/htdocs\/chall/g' /etc/apache2/httpd.conf

RUN echo "php_value error_reporting 1" >> /etc/apache2/httpd.conf
RUN echo "php_flag magic_quotes_gpc Off" >> /etc/apache2/httpd.conf
RUN echo "php_value magic_quotes_gpc Off" >> /etc/apache2/httpd.conf
RUN echo "Options +FollowSymLinks" >> /etc/apache2/httpd.conf

RUN /entrypoint.sh

COPY run_services.sh run_services.sh
CMD ./run_services.sh
