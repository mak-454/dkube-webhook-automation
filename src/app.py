from github_webhook import Webhook
from flask import Flask
import os
import requests

from dkube.sdk.dkube import *
import yaml 

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def ping():
    return "Alive!!"


@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    dkube()

def dkube():
    input_yaml = open('/etc/automation.yaml', 'r') 
    inputs = input_yaml.read() 
    inputs = yaml.safe_load(inputs) 
    print("Inputs -> ", inputs)
    env = Environment(scheme='https', host=inputs['host'], user=inputs['user'], token=inputs['token'], port=32222) 
    launch_training_job(inputs['jobname'], autogenerate=True, environ=env.external,workspace=inputs['workspace'], script=inputs['script'],datasets=inputs['datasets'],models=inputs['models'], template='')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

