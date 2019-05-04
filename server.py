from threading import Lock
from flask import Flask, Response, request, url_for, jsonify, render_template, session
from flask_socketio import SocketIO, emit, disconnect
import os

app = Flask(__name__)

async_mode = None
socketio = SocketIO(app, async_mode=async_mode)

users = {"U0ZFL9KA9" : "Connor", "U95EEL17H":"Chieco", "U0ZFZ0U1M":"Rushabh", "U44BENMLZ":"Calvin", "U451ZSLD8":"Tyler", "U0M121CV7":"Foreman", "U0ZFGNE3F":"Poli", "U44AMB57S":"Noah", "U454LRGLD":"Jack"}

app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def printSup():
    jdata = request.get_json()
    print("the request: was received")
    try:
        try:
            challenge = jdata['challenge']
            return challenge
        except:
            print("no challenge")
        event = jdata['event']
        print(event)
        #bwh is C0T96JKCY
        if (event['channel'] == 'C0T96JKCY'):
            print("\ndispatching bump\n")
            try:
                print(event['user'])
                print(users[event['user']])
                try:
                    user = users[event['user']]
                except:
                    user = "Chieco"
            except:
                user = "Chieco"
            socketio.emit('bump', {'name' : user})
        else:
            print("\ndispatch failed\n")
    except(e):
        print("\nparse failed\n")
    #weird hack but ok
    return("adsfads")

def processrequest(request):
    print("hey im python")
if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=7003)
