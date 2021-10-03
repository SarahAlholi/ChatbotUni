# FROM ubuntu:18.04
# ENTRYPOINT ["/app/server.sh"]
# RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.3.4
# WORKDIR /app

# # ADD requirements.txt .

# # RUN pip install -r requirements.txt --no-cache-dir

# COPY app /app
# COPY server.sh /app/server.sh

# USER root

# RUN rasa train
# RUN chmod a+rwx /app/server.sh

# EXPOSE 5005

# CMD python3 actions/actions.py -d models -u models --port $PORT -o log_file.log
FROM ubuntu:18.04
FROM rasa/rasa_core_sdk:latest
FROM python:3.7-slim


RUN python -m pip install rasa
# RUN python3 -m http.server

WORKDIR /app
COPY . .
COPY index.html /
COPY server.sh /app/server.sh

RUN rasa train 

RUN chmod a+rwx /app/server.sh
USER 1001

ENTRYPOINT [ "rasa" ]
EXPOSE 5005

CMD [ "run","--enable-api","--port","5005" ]




