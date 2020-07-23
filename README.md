# flask-websocket

[![Build Status](https://travis-ci.com/chrisborbidge/flask-websocket.svg?branch=master)](https://travis-ci.com/chrisborbidge/flask-websocket)

Long running task, communicating via. websockets, powered by Flask. 

### Quick start

#### Development
```
python -m venv .venv
pip install -r "requirements.txt"
python3 application.py
```

#### Production
```
pip install -r "requirements.txt"
gunicorn application:app
```
