from flask import Flask, Response, abort

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
