
SQL_FILE=./SQL/codenutv2.sql

cd /root/CodeNut &&
    git pull &&
    docker cp $SQL_FILE mysql:/tmp/1 &&
    docker exec mysql bash -c "mysql -proot codenut < /tmp/1" &&
    docker exec flask bash -c "python3 ./download_answer.py && supervisorctl restart all" 