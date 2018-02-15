# CREDO API service

This package is a reference implementation of API used by CREDO software stack.

## Development and installation
All of the configuration variables are handled by supplying an env var, or directly changing the `config.py` file.

Env is controlled through `pipenv`, packaging is done with `easy_install`.


## Contributing

Fork & develop & pull request


## API description

### Submit detection report

Every user with a valid access token is able to submit a detection report. The submission is done by sending a POST request to specified endpoint:

```bash
POST /detection
```

with a json payload, which should follow this example:

```json
{
    "body": {
        "detection": {
            "accuracy": 1.0,
            "altitude": 1.0,
            "frame_content": "base64 of png image data",
            "height": 40,
            "width": 40,
            "id": 1,
            "latitude": 50.000000,
            "longitude": 20.000000,
            "provider": "provider name",
            "timestamp": 1518707872
        },
        "device_info": {
            "androidVersion": "7.0",
            "deviceId": "device Id",
            "deviceModel": "device model"
        },
        "user_info": {
            "email": "user@email.com",
            "key": "access_key",
            "name": "name",
            "team": "team"
        }
    },
    "header": {
        "application": "1.3",
        "frame_type": "detection",
        "protocol": "1.0",
        "time_stamp": 1518707872
    }
}
```

The message is composed from the following parts:
* body - contains the detection data like accuracy, image, localization and timestamp 
* device_info - information about the detecting device
* user_info - used data and access key
* header - metadata, protocol version

All fields are mandatory. Upon successful submission a `HTTP 201 Created` response code is returned. In case of any problems with parsing the data a `HTTP 403 Unprocessable entity` is returned.

### Retrieve detection report

Detection reports can be retrieved by supplying a detection owner's api key and a timestamp.

```bash
GET /detection/:user_name/:timestamp
```

Returned JSON is the exact content supplied by a `POST` operation above. Upon success a `HTTP 200 OK` code is returned, and `HTTP 404 Not Found` if a desired report cannot be retrieved.

### Retrieve detection image

Individual images can be retrieved by supplying in a similar fashion as complete reports.

```bash
GET /detection_image/:user_name/:timestamp
```

Returned image is supplied in raw format and can be displayed by any browser. Successful retrieval is signaled with a `HTTP 200 OK` and `HTTP 404 Not Found` is returned if an image is unavailable.

### Unexpected errors

In case of any server side issues a `HTTP 500 Internal Server Error` status code is returned. 

## Authors
* Maciej Pawlik <m.pawlik@cyfronet.pl>
* Reserved for you