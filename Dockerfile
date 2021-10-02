FROM ubuntu:18.04
ENTRYPOINT ["/app/server.sh"]
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.3.4
WORKDIR /app

# ADD requirements.txt .

# RUN pip install -r requirements.txt --no-cache-dir

COPY app /app
COPY server.sh /app/server.sh

USER root

RUN rasa train
RUN chmod a+rwx /app/server.sh

EXPOSE 5005

CMD python3 actions/actions.py -d models -u models --port $PORT -o log_file.log






