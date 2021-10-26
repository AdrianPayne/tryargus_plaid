from flask import Flask, request, Response, abort
import os
import requests
import json

from plaid_client import CLIENT_ID, SECRET, ENV_URL


# Cache vars
access_token = None
investment_and_transaction_data = None

# flask app
application = Flask(__name__)


@application.route("/", methods=['GET'])
def healthy():
    return Response("Healthy", status=200)


@application.route("/exchange", methods=['POST'])
def exchange():
    body = request.get_json()
    public_token = body['public_token']

    url = ENV_URL + "item/public_token/exchange"
    payload = json.dumps({
        "client_id": CLIENT_ID,
        "secret": SECRET,
        "public_token": public_token
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    global access_token
    access_token = response.json()['access_token']

    return Response(status=201)


@application.route("/query", methods=['POST'])
def query():
    url = ENV_URL + "investments/holdings/get"

    if access_token is None:
        abort(404)

    payload = json.dumps({
        "client_id": CLIENT_ID,
        "secret": SECRET,
        "access_token": access_token
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    global investment_and_transaction_data
    investment_and_transaction_data = response

    return Response(status=201)


@application.route("/account", methods=['GET'])
def account():
    return Response(investment_and_transaction_data, status=201)


if __name__ == '__main__':
    application.run(port=os.getenv('PORT', 5000))
