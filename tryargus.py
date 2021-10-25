from flask import Flask, Response, abort
import os

import plaid
from plaid.api import plaid_api

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': 'client_id',
        'secret': 'secret',
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)


# flask app
app = Flask(__name__)


@app.route("/", methods=['GET'])
def healthy():
    return Response("Healthy", status=200)


@app.route("/exchange", methods=['POST'])
def exchange():
    return Response(status=201)


@app.route("/query", methods=['POST'])
def query():
    response = True
    if response:
        abort(404)
    return Response(status=201)


@app.route("/account", methods=['GET'])
def account():
    data = ""
    return Response(data, status=201)


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000))
