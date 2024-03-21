from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    container_ip = socket.gethostbyname(hostname)
    return render_template('index.html', container_ip=container_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
