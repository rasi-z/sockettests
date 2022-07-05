from flask_socketio import SocketIO,send
from flask import Flask
from numpy import broadcast

app=Flask(__name__)
s = SocketIO(app, cors_allowed_origins="*")

@s.on('connect')
def d(msg):
    print(msg)


@s.on('text')
def m(msg):
        print(msg[0],msg[1])
        s.emit('idm',msg,broadcast=True)



if __name__=='__main__':
    s.run(app)
    