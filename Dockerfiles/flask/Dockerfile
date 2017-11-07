
FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./judge_src /tmp/judge_src
COPY ./requirements.txt /tmp/requirements.txt
COPY ./install_env.sh /tmp/install_env.sh

RUN apt-get update && apt-get install -y git supervisor sudo systemd
RUN /bin/bash /tmp/install_env.sh
RUN pip3 install -r /tmp/requirements.txt
RUN cd /tmp/judge_src && python3 ./setup.py install

ENTRYPOINT /bin/bash /opt/CodeNut/start_app.sh && /bin/bash
