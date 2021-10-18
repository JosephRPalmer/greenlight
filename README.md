# signalman
A small application to poll a remote endpoint for response code or text.

## How to use signalman

`signalman --timeout 60 --endpoint google.com --port 80 --rc 200` will run a test for 60 minutes until google.com returns a HTTP 200 on port 80


## Parameter List

| Syntax | Description |
| ----------- | ----------- |
| --timeout | Timeout for Signalman in minutes |
| --endpoint | URL to test against |
| --port | Port to test against |
| --rc (optional) | Return code which you are looking for/expecting |
| --rtext (optional) | Return text you are looking for/expecting |
| --ssl (optional) | Use SSL/TLS |
| --headers (optional) | Any headers which need to be included - for example to request Content-Type: application/json use h.content-type:application/json |
