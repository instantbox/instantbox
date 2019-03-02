#!/bin/python

import re
import os
import sys
import json
import time
import random
import string
import subprocess
from flask_cors import CORS
from api.redisCli import ConnectRedis
from api.rmContainer import RmContainer
from flask import render_template, redirect
from api.createContainer import CreateContainer
from flask import Flask, request, Response, jsonify

app = Flask(__name__)
CORS(app, resources=r'/*')

redisCli = ConnectRedis()
create_container_client = CreateContainer()
rm_container_client = RmContainer()

SERVERURL = os.environ.get('SERVERURL')

OS_LIST = None
with open("manifest.json", "r") as os_manifest:
    OS_LIST = json.load(os_manifest)
if OS_LIST is None:
    raise Exception('Could not load manifest.json')

AVAILABLE_OS = []
for os in OS_LIST:
    for ver in os['subList']:
        AVAILABLE_OS.append(ver['osCode'])


def randPort():
    rand_port = random.randint(1, 65536)
    if (6000 <= rand_port <= 7000) or (rand_port == 22):
        randPort()
    else:
        try:
            subprocess.check_output("lsof -i:%s" % (rand_port), shell=True)
        except subprocess.CalledProcessError:
            return rand_port
        else:
            randPort()


def genString():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return salt


@app.route('/v2/superinspire/getOSList')
def returnList():

    response = Response(json.dumps(OS_LIST), mimetype='application/json')

    response.headers.add('Server', 'python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route('/v2/superinspire')
def hello():
    return 'hello'


@app.route('/v2/superinspire/rmOS')
def rmOS():
    try:
        containerId = request.args.get("containerId")
        timestamp = request.args.get("timestamp")
        shareUrl = request.args.get("shareUrl")
    except Exception:
        response = Response(
            json.dumps({
                "message": "Arguments ERROR",
                "statusCode": 0
            }),
            mimetype='application/json')
    else:
        if redisCli.is_container(containerId):
            try:
                isSuccess = rm_container_client.is_rm_container(containerId)
                if not isSuccess:
                    raise Exception

            except Exception:
                response = Response(
                    json.dumps({
                        "message": "RM docker containers ERROR",
                        "shareUrl": "",
                        "statusCode": 0,
                    }),
                    mimetype='application/json')
            else:
                response = Response(
                    json.dumps({
                        "message": "SUCCESS",
                        "statusCode": 1,
                        "containerId": containerId,
                    }),
                    mimetype='application/json')
        else:
            response = Response(
                json.dumps({
                    "message": "docker containers not exist ERROR",
                    "statusCode": 0,
                    "containerId": containerId,
                }),
                mimetype='application/json')

    response.headers.add('Server', 'python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route('/v2/superinspire/getOS')
def getOS():

    shareUrl = "http://{0}:{1}"
    openPort = ''

    try:
        os_name = request.args.get("os")
    except Exception:
        response = Response(
            json.dumps({
                "message": "OS Arguments ERROR",
                "statusCode": 0
            }),
            mimetype='application/json')
    else:
        try:
            os_mem = request.args.get("mem")
            os_cpu = request.args.get("cpu")
            os_port = request.args.get("port")
            os_timeout = request.args.get("timeout")
        except Exception:
            if os_name not in AVAILABLE_OS:
                response = Response(
                    json.dumps({
                        "message":
                        "The image is not supported at this time ERROR",
                        "statusCode": 0
                    }),
                    mimetype='application/json')
        else:

            if os_mem is None:
                os_mem = 512
            if os_cpu is None:
                os_cpu = 1
            if os_timeout:
                os_timeout = 3600 * 24 + time.time()

            rand_string = genString()
            webShellPort = randPort()
            try:
                if os_port is None:
                    isSuccess = create_container_client.is_create_container(
                        mem=os_mem,
                        cpu=os_cpu,
                        web_shell_port=webShellPort,
                        container_name=rand_string,
                        os_name=os_name,
                    )

                else:
                    openPort = randPort()
                    isSuccess = create_container_client.is_create_container(
                        mem=os_mem,
                        cpu=os_cpu,
                        web_shell_port=webShellPort,
                        container_name=rand_string,
                        os_name=os_name,
                        open_port=os_port,
                        rand_port=openPort)

                if not isSuccess:
                    raise Exception
            except Exception:
                response = Response(
                    json.dumps({
                        "message": "RUN docker containers ERROR",
                        "shareUrl": "",
                        "statusCode": 0,
                    }),
                    mimetype='application/json')
            else:
                redisCli.set_container(rand_string)

                response = Response(
                    json.dumps({
                        "message":
                        "SUCCESS",
                        "shareUrl":
                        shareUrl.format(SERVERURL, webShellPort),
                        "openPort":
                        openPort,
                        "statusCode":
                        1,
                        "containerId":
                        rand_string,
                    }),
                    mimetype='application/json')

    response.headers.add('Server', 'python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=int(65501), debug=False)
