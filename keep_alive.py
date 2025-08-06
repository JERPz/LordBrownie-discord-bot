from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Meow~ I'm alive and paw-some!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
