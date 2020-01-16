from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from random import random
from time import sleep
from threading import Thread, Event

app = Flask(__name__)

socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

thread = Thread()
thread_stop_event = Event()


def generate_random_number():
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    """
    print("Generate random numbers...")
    while not thread_stop_event.isSet():
        number = round(random() * 10, 3)
        print(number)
        socketio.emit("new_number", {"number": number}, namespace="/random")
        socketio.sleep(5)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect", namespace="/random")
def random_connect():
    global thread
    print("Client connected!")

    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(generate_random_number)


@socketio.on("disconnect", namespace="/random")
def random_disconnect():
    print("Client disconnected!")


if __name__ == "__main__":
    socketio.run(app)
