FROM rasa/rasa:1.9.3

USER root

RUN rasa train
RUN chmod a+rwx /ChatbotUniAssistant/server.sh

ENTRYPOINT ["/ChatbotUniAssistant/server.sh"]