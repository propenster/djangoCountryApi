# djangoCountryApi
A RESTful API endpoint for country codes, names and population made with the pythonic Django Rest Framework

## API Search Endpoint

### Request
   GET  /countries/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

### Response
[
    {
        "code": "AU",
        "name": "Australia",
        "population": 24016400
    },
    {
        "code": "BR",
        "name": "Brazil",
        "population": 205722000
    },
    {
        "code": "CA",
        "name": "Canada",
        "population": 35985751
    },
    {
        "code": "CN",
        "name": "China",
        "population": 1375210000
    },
    {
        "code": "DE",
        "name": "Germany",
        "population": 81459000
    },
    {
        "code": "FR",
        "name": "France",
        "population": 64513242
    },
    {
        "code": "GB",
        "name": "United Kingdom",
        "population": 65097000
    },
    {
        "code": "IN",
        "name": "India",
        "population": 1285400000
    },
    {
        "code": "RU",
        "name": "Russia",
        "population": 146519759
    },
    {
        "code": "US",
        "name": "United States of America",
        "population": 322976000
    },
    {
        "code": "NG",
        "name": "Nigeria",
        "population": 200000000
    }
]
