# Vue Timezones

## Setup 

In order to get the app running, server and client dependencies must be installed. 

To get server side dependencies installed run `pipenv install` or `pip install flask flask-cors arrow ` in the case that pipenv install isn't functioning correctly.

To launch the server run `python server.py`. At this point if you make a GET request to http://localhost:9123 it should return an affirmative message.

To get the client up and running, move into the client directory and run `npm install` to get all dependencies installed. 

Once everything is installed, running `npm run serve` will get the client running and serve you a link you can follow to interact with the client, usually http://localhost:8080

Once both the server and client are running you should be free to use the app.

## Endpoints 

The Flask API has 2 endpoints

### / 

The root endpoint only exists to confirm the backend is functioning properly. Sending a GET request to the root endpoint should return the message "Flask app live" if everything is functioning properly.

### /convert

The convert endpoint accepts a POST request with a time to convert as well as the timezones to convert to and from, and returns the converted time as well as if Daylight Savings Time is currently active in the returned time.

#### Example Body
```
{
    "datetime": "2021-11-07 00:00",
    "from_TZ": "EST",
    "to_TZ": "Central Standard Time"
}
```

#### Parameters

* `datetime` string in format `YYYY-MM-DD HH:mm`, time to be converted 
* `from_TZ` string in formats detailed below, timezone time is being sent in
* `to_TZ` string in formats detailed below, timezone time should be converted to

Timezone formats accepted include<sup id='a1'>[1](#foot1)</sup>:

* A str describing a timezone, similar to ‘US/Pacific’, or ‘Europe/Berlin’.
* A str in ISO 8601 style, as in ‘+07:00’.
* A str, one of the following: ‘local’, ‘utc’, ‘UTC’.

#### Example Return

The body sent above would return the JSON object below

```
{
    "is_DST": true,
    "time": "2021-11-07 00:00:00-05:00"
}
```

## Design decisions

* I deliberated for some time on how best to convert time zones. I made an initial mockup using a JSON of timezones and offsets to keep from leaning on external packages, but ended up using the [**arrow**](https://arrow.readthedocs.io/en/stable/) package for a couple of reasons:

    * It was difficult to find a good source of truth regarding timezones and offsets online. I tried a few but they ended up being either inaccurate or too vague to be useful

    * In pursuit of accuracy there are far too many edge cases to account for and stay within a reasonable scope, i.e. leap years and daylight savings differences 

<sup id='foot1'>1</sup>: Taken from the [Arrow API Guide](https://arrow.readthedocs.io/en/stable/#api-guide) and modified for the purposes of this project [↩](#a1)