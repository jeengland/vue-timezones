from flask import Flask, request
import datetime
import arrow


app = Flask(__name__)


# Test endpoint
@app.route('/')
def running():
    return 'Flask app live'


if __name__ == '__main__':
    app.run(host='localhost', port='9123')
