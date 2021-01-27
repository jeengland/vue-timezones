from flask import Flask, request
from flask_cors import CORS
import datetime
import arrow


app = Flask(__name__)
CORS(app)


# Test endpoint
@app.route('/')
def running():
    return 'Flask app live'


# Conversion endpoint
# Accepts JSON object with the following parameters
# datetime - string; time to convert from with format YYYY-MM-DD HH:mm
# from_TZ - string indicating timezone time is being delivered in
# to_TZ - string indicating timezone to convert to
@app.route('/convert', methods=['POST'])
def convert_time():
    time = request.json['datetime']
    from_TZ = request.json['from_TZ']
    to_Tz = request.json['to_TZ']
    # All this is necessary to get the data into a datetime format,
    # which in turn is necessary to get user inputted times into
    # the proper arrow format for some reason
    year = int(time[0:4])
    month = int(time[5:7])
    day = int(time[8:10])
    hour = int(time[11:13])
    minute = int(time[14:])
    time = datetime.datetime(year, month, day, hour, minute, 0, 0)
    # The actual conversion is handled by an external library for reasons
    # outlined in the README
    converted = arrow.get(time, from_TZ).to(to_Tz)
    # This is the check to see if DST is active
    dl = True if str(converted.dst()) == '1:00:00' else False
    # Returned object includes time as well as if the timezone in
    # question is in DST
    return {'time': converted.format(), 'is_DST': dl}


if __name__ == '__main__':
    app.run(host='localhost', port='9123')
