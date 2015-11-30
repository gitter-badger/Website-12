#!/usr/bin/env python3
from __future__ import unicode_literals
import os
import sys
from flask import Flask, send_from_directory, request

app = Flask(__name__, static_url_path='')
app.debug = True

path = os.path.dirname(os.path.abspath(__file__))

@app.route('/') 
def root():
    return """
<!doctype html>
<html>
    <head>
        <title>FSM Belgium</title>
    </head>
    <body style="margin:0;">
        <img style="width:100%;" src="data/fsm.jpg">
    </body>
    <div></div>
</html>
"""

@app.route('/data/<path:path>')
def send_js(path):
    return send_from_directory('/var/www/fsmbelgium.com/html/data', path)
    
    
if __name__ == '__main__':
    app.run()
