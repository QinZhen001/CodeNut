FROM mysql:latest
# RUN echo "\n[mysqld]\nserver-id=1\nlog-bin=binlog\nperformance_schema=OFF\ntable_definition_cache=400\ntable_open_cache=256" >> /etc/mysql/my.cnf
COPY ./codenut.sql docker-entrypoint-initdb.d/codenut.sql
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE codenut
