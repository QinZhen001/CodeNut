# docker file description

# before all of this
apt-get update && apt-get install -y git
git clone --branch all --single-branch -- https://github.com/QinZhen001/CodeNut.git /root/CodeNut
cp -r /root/Codenut/CodeNutJudge/judge_src /root/CodeNut/Dockerfiles/flask/
cp /root/CodeNut/CodeNutJudge/install_env.sh /root/CodeNut/Dockerfiles/flask/
cp /root/CodeNut/CodeNutAPI/requirements.txt /root/CodeNut/Dockerfiles/flask/
cp /root/CodeNut/SQL/codenut.sql /root/CodeNut/Dockerfiles/mysql/
# docker build process
docker build --tag codenut/flask /root/CodeNut/Dockerfiles/flask/
docker build --tag codenut/redis /root/CodeNut/Dockerfiles/redis/
docker build --tag codenut/mysql /root/CodeNut/Dockerfiles/mysql/

# docker running process
docker run --detach --name redis codenut/redis
docker run --name mysql --detach codenut/mysql
docker run --detach -it --name flask --publish 5000:5000 --link redis:appredis --link mysql:appmysql --volume /root/CodeNut:/opt/CodeNut --workdir /opt/CodeNut codenut/flask


# clean
#trash /root/CodeNut
#docker rm redis mysql flask
#docker rmi codenut/mysql codenut/flask codenut/redis

cd /root/CodeNut/Dockerfiles/flask
rm -r -f judge_src install_env.sh requirements.txt
cd /root/CodeNut/Dockerfiles/mysql
rm -f codenut.sql
