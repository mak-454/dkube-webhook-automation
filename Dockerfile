FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y gunicorn git

RUN pip3 install flask flask_cors flask_restful requests gunicorn github_webhook futures

RUN pip3 install setuptools wheel  

RUN pip3 install git+https://github.com/oneconvergence/dkube.git@1.5

ENV PYTHONPATH "${PYTHONPATH}:/home/dkube/py/"

RUN useradd -d /home/dkube -ms /bin/bash -g root -G sudo -p dkube dkube

USER dkube

WORKDIR /home/dkube

LABEL heritage="dkube"

COPY src/* /home/dkube/py/

CMD ["gunicorn", "--worker-class=gevent", "--worker-connections=1000", "--workers=8", "-k", "gthread", "--threads", "8", "app:app", "--bind", "0.0.0.0:8000"]
