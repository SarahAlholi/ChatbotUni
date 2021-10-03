FROM ubuntu:18.04
FROM rasa/rasa-sdk:1.8.1 
USER root

RUN pip --no-cache-dir install requests
USER 1001

FROM python:3.6-slim

ENTRYPOINT ["/app/server.sh"]
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.3.4
WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .
COPY server.sh /app/server.sh

RUN rasa train
RUN chmod a+rwx /app/server.sh

EXPOSE 5005

CMD python3 actions/actions.py -d models -u models --port $PORT -o log_file.log

# # use a python container as a starting point
# # Extend the official Rasa SDK image
# FROM rasa/rasa-sdk:1.8.1 
# USER root
# # Add a custom python library (e.g. jupyter)
# RUN pip --no-cache-dir install requests
# USER 1001

# FROM python:3.6-slim

# # install dependencies of interest
# RUN python -m pip install rasa[spacy] && \
#     python -m spacy download en_core_web_lg

# # set workdir and copy data files from disk
# # note the latter command uses .dockerignore
# WORKDIR /app
# ENV HOME=/app
# COPY . .

# # train a new rasa model
# RUN rasa train 

# # set entrypoint for interactive shells
# ENTRYPOINT ["rasa"]

# # command to run when container is called to run
# CMD ["run", "--enable-api", "--port", "8080"]



# FROM ubuntu:18.04
# FROM rasa/rasa_core_sdk:latest
# FROM python:3.7-slim


# RUN python -m pip3 install rasa
# # RUN python3 -m http.server

# WORKDIR /app
# COPY . .
# COPY index.html /
# COPY server.sh /app/server.sh

# RUN rasa train 

# RUN chmod a+rwx /app/server.sh
# USER 1001

# ENTRYPOINT [ "rasa" ]
# EXPOSE 5005

# CMD [ "run","--enable-api","--port","5005" ]




