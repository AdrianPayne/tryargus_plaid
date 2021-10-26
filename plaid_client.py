import requests
import json
import os

# ENV
CLIENT_ID = '6176e5e044fc260012f975b7'
SECRET = '971eb8b7fc5751caee53cb59bc7bc8'
ENV_URL = 'https://sandbox.plaid.com/'


def get_public_token():
    url = ENV_URL + "sandbox/public_token/create"

    payload = json.dumps({
      "client_id": CLIENT_ID,
      "secret": SECRET,
      "institution_id": "ins_3",
      "initial_products": [
        "auth"
      ],
      "options": {
        "webhook": "https://www.genericwebhookurl.com/webhook"
      }
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['public_token']