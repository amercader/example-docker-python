from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    if request.remote_addr:

        url = 'http://freegeoip.net/json/{0}'.format(request.remote_addr)
        r = requests.get(url).json()
        return "Hi, it looks like you are around {0}.".format(r['city'])
    else:
        return "Hi, we don't know where you are."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
