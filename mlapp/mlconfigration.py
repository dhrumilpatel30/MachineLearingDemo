import urllib.request
import json
import os
import ssl
from decouple import config


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if (
        allowed
        and not os.environ.get("PYTHONHTTPSVERIFY", "")
        and getattr(ssl, "_create_unverified_context", None)
    ):
        ssl._create_default_https_context = ssl._create_unverified_context


def Calculate(form_data):
    allowSelfSignedHttps(
        True
    )  # this line is needed if you use self-signed certificate in your scoring service.

    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script

    data = {
        "Inputs": {"data": [form_data]},
        "GlobalParameters": 0.0,
    }
    print(data)
    body = str.encode(json.dumps(data))

    url = "http://c12792b1-ec04-4c37-ac90-8140af8e7225.centralindia.azurecontainer.io/score"
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = config("API_KEY")
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    headers = {
        "Content-Type": "application/json",
        "Authorization": ("Bearer " + api_key),
    }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", "ignore"))
