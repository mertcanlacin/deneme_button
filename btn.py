from flask import Flask, render_template, request, redirect, url_for
from time import sleep
from threading import Thread
import serial
import time
from pyfirmata2 import Arduino
import http.client

PIN = 13


board = Arduino('/dev/ttyACM0')



app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def hello_world():
    if request.method == 'POST':
        if request.form['submit'] == 'Turn On':
            print ('TURN ON')
            board.digital[PIN].write(1)
        elif request.form['submit'] == 'Turn Off':
            print ('TURN OFF')
            board.digital[PIN].write(0)

        else:
            pass

    return render_template('index.html')


if __name__ == '__main__':

    app.run(port=5000, host='localhost', debug = True)
