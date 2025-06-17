from flask import Flask, jsonify
from datetime import datetime
import socket



app = Flask(__name__)

@app.route('/api/v1/details')

def detailes():
#    return '<h1>Hello World</h1>'
     return jsonify({
          'time' : datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
          'hostname': socket.gethostname()
          'messages': 'You are doing great, human!'
          
     })

@app.route('/api/v1/healthz')

def health():
     return jsonify({
          'status': 'up'
          
     }), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")

#'/api/v1/details'
#'/api/v1/healthz'