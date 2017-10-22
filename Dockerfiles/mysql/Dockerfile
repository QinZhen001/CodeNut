FROM mysql:latest
RUN echo "\n[mysqld]\nserver-id=1\nlog-bin=binlog\nperformance_schema=OFF\ntable_definition_cache=400\ntable_open_cache=256" >> /etc/mysql/my.cnf

RUN service mysql restart && \
    mysql -uroot -proot --execute="UPDATE mysql.user SET Password=PASSWORD('root') WHERE USER='root'; FLUSH PRIVILEGES; CREATE DATABASE codenut" && \
    mysql -uroot -proot codenut < codenut.sql && \
