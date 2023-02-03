from flask import Flask, render_template
from flask_sock import Sock
import json
import time, datetime
import threading

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')

def send_time(ws):
    while True:
        time.sleep(1)
        try:
            ws.send(json.dumps({"type": "clock", "text": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}))
        except:
            break

@sock.route('/echo')
def echo(ws):
    t = threading.Thread(target=send_time,args=(ws,))
    t.start()
    while True:
        data = ws.receive()
        if data == 'close':
            break
        ws.send(json.dumps({"type": "log", "text": data}))

if __name__ == '__main__':
    app.run()
