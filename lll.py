import RPi.GPIO as gp
from flask import Flask
import threading
import time 
app = Flask(__name__)

def blink ():
    while True:
        global val
        if val == 2:
            break
        gp.output(25, gp.HIGH)
        time.sleep(1)
        gp.output(25,gp.LOW)
        time.sleep(1)
        
@app.route('/ledon')
def ledon():
    global val
    val = 2
    gp.output(25, gp.LOW)
    return 'ledon'

@app.route('/ledoff')
def ledoff():
    global val
    val = 2
    gp.output(25, gp.HIGH)
    return 'ledoff'
    
@app.route('/start')
def ledloop():
    global val
    val = 1
    t = threading.Thread(target = blink)
    t.start()
    return 'yeah'

@app.route('/ledstop')
def ledstop():
    global val
    val = 2
    return 'stop'

if __name__ == '__main__':
    global val
    val = 1
    gp.setmode(gp.BCM)
    gp.setup(25, gp.OUT)
    gp.output(25, gp.HIGH)
    app.run()