#!/bin/bash

table='codenut'
for i in `mysql -uroot -proot -N -e "select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA=\"${table}\"" | awk '{print $1}'`; do
  echo ${i}
  mysql -uroot -proot -e "show COLUMNS from ${table}.${i}"
done
