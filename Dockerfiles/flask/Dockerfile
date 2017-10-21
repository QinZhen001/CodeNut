
FROM tiangolo/uwsgi-nginx-flask

RUN apt-get update && apt-get install -y git supervisor sudo systemd

COPY /root/CodeNut/CodeNutAPI/requirements.txt /tmp/requirements.txt
COPY /root/CodeNut/CodeNutAPI/gunicorn.conf /etc/gunicorn.conf
COPY /root/CodeNutJudge/install_env.sh /tmp/install_env.sh
RUN /bin/bash /tmp/install_env.sh
RUN pip3 install -r /tmp/requirements.txt

COPY /root/CodeNutJudge/judge_src /tmp/judge_src
RUN cd /tmp/judge_src && python3 ./setup.py install

CMD ["/bin/bash","/opt/CodeNut/start_app.sh"]
    
    
