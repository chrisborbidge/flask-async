# flask-async

Long running task, communicating via. websockets, powered by Flask. 

### Quick start

#### Development
```
python -m venv .venv
pip install -r "requirements.txt"
python3 app.py
```

#### Production
```
pip install -r "requirements.txt"
gunicorn app:app
```

### Demo

#### Production
https://flask-async.onrender.com/

#### Development
https://flask-async-development.onrender.com/
