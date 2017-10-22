# docker file description

# before all of this
apt-get update && apt-get install -y git docker.io
git clone --branch all --single-branch -- https://github.com/QinZhen001/CodeNut.git /root/CodeNut

# docker build process
docker build --tag codenut/flask /root/CodeNut/Dockerfiles/flask/
docker build --tag codenut/redis /root/CodeNut/Dockerfiles/redis/
docker build --tag codenut/mysql /root/CodeNut/Dockerfiles/mysql/

# docker running process
docker run --detach --name redis codenut/redis
docker run --detach --name mysql codenut/mysql
docker run --detach --name flask --publish 5000:80 --link redis:appredis --link mysql:appmysql --volume /root/CodeNut:/opt/CodeNut --workdir /opt/CodeNut codenut/flask


# clean
trash /root/CodeNut
docker rmi codenut
docker rm redis mysql flask
