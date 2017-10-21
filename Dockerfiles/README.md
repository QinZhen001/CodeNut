# docker file description

# before all of this
git clone --branch all --single-branch -- https://github.com/QinZhen001/CodeNut.git /root

# docker build process
docker build --tag codenut/flask ./Dockerfiles/flask/
docker build --tag codenut/redis ./Dockerfiles/redis/
docker build --tag codenut/mysql ./Dockerfiles/mysql/

# docker running process
docker run --detach --name redis codenut/redis
docker run --detach --name mysql codenut/mysql
docker run --detach --name flask --publish 5000:80 --link redis:redis --link mysql:mysql --volume /root/CodeNut:/opt/CodeNut --workdir /opt/CodeNut codenut/flask 
