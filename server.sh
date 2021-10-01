python3 -m rasa run actions —- actions actions -p 5055 —- debug >> 
/Users/sarahalhouli/ChatbotUniAssistant/logs/rasa_action-`/bin/date +\%Y-\%m-\%d-\%H-\%M-\%S`.log 2>&1

python3 -m rasa run -m models — endpoints endpoints.yml -p 5005 — enable-api 
-— credentials credentials.yml -— log-file /Users/sarahalhouli/ChatbotUniAssistant/logs/rasa_core-`/bin/date +\%Y-\%m-\%d-\%H-\%M-\%H-\%M-\%S`.log —- debug

python3 nlg_server.py -d domain.yml &