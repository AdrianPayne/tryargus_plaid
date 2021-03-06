# Tryargus Plaid
## Flask API connected to a third party
Simple flask API that connects to a 3rd party API (Plaid) in order to
read, store (in memory), and serve some data.

## Description
Using the sandbox environment of [Plaid](https://plaid.com/en-eu/). Build a simple API with the following resources:

Resource | Method | BODY | RESPONSE
---------| ------ | ---- | -------
/ | GET | - | 200 "Healthy"
/exchange | POST | {“public_token”: “<public_token>”} | 201
/query | POST | - |  <ul><li>If called before “/exchange”, returns a 404</li><li>201</li></ul>
/account | GET | - | 200 & response from “/query”

## Local use
### Deploy
Create and activate local environment
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
Deploy locally
```
python3 application.py
```
Now it is working in http://127.0.0.1:5000/


### Test
Only execute
````
py.test -vv --disable-pytest-warnings
````
I had used **pytest-ordering** to avoid cache problems between tests

## AWS Instance
http://flask-env.eba-pxrp9ipm.us-east-2.elasticbeanstalk.com/

## Postman Collection
Local and AWS
https://www.getpostman.com/collections/b301c1865c145436f3bf

## Roadmap
- [x] Create account in Plaid
- [x] Create Integration test suit
- [x] Build the resource API skeleton
- [x] Create methods to call the API
- [x] Complete the test suit
- [X] Create an AWS instance and deploy it
- [X] Postman collection

## Notes
1. As it is a test in a sandbox environment and to facilitate the tests by third parties, I have not encrypted the 
   sensitive information to connect with the Plaid API. Of course, this is something to be avoided in real projects 
   (using AWS env or GitHub Actions for example).
   
2. I have preferred to use http requests directly because **Plaid PostMan collection** has better explained and completed 
than **Plaid python library** documentation.
   
3. For the same reason of Note 1, I have not configured any security in AWS instance (all directions allowed). Obviously 
it is only for a test case.