FROM ubuntu:18.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.3.4
WORKDIR /ChatbotUni

ADD requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . /ChatbotUni/

EXPOSE 5005

CMD python3 /server.py -d models -u models --port $PORT -o log_file.log


# FROM rasa/rasa:1.9.3

# USER root

# RUN rasa train
# RUN chmod a+rwx /ChatbotUniAssistant/server.sh

# ENTRYPOINT ["/ChatbotUniAssistant/server.sh"]