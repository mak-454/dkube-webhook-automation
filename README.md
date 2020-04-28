This repo contains code to showcase dkube automation with github webhooks.

## src/app.y
Built using project @ https://github.com/bloomberg/python-github-webhook

On a push event (commit) uses dkube SDK @ https://github.com/oneconvergence/dkube.git@1.5
to trigger an ML training run on the specified cluster with specified code, dataset etc...

Cluster settings, auth token, code, dataset can be configured in automation.yaml

## How to build container
To build a new container image --> docker build -t <registry/image:tag> .

There is a pre-built public image availabe @ ocdr/dkube-webhook-automation:2.0

## How to run
- Webhook server runs inside a container.
- Download automation.yaml and edit as per the deployment.

docker run -it -p 80:8000 -v {PATH}/automation.yaml:/etc/automation.yaml ocdr/dkube-webhook-automation:2.0


## Please make sure that cluster is reachable from the node where this container is run
