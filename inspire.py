#!/bin/python

import re
import os
import json
import time
from flask_cors import CORS
from flask import render_template, redirect
from flask import Flask, request, Response, jsonify
from api.instantboxManager import InstantboxManager

app = Flask(__name__)
CORS(app, resources=r'/*')

instantboxManager = InstantboxManager()

SERVERURL = os.environ.get('SERVERURL')
if SERVERURL is None:
    SERVERURL = ''

SWARM_MODE = False
if os.environ.get('SWARM_MODE') == '1' :
    SWARM_MODE = True

@app.route('/v2/superinspire')
def hello():
    return 'hello'


@app.route('/v2/superinspire/getOSList')
def returnList():

    response = Response(
        json.dumps(instantboxManager.OS_LIST), mimetype='application/json')

    response.headers.add('Server', 'python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route('/v2/superinspire/rmOS')
def rmOS():
    try:
        containerId = request.args.get('containerId')
        timestamp = request.args.get('timestamp')
        shareUrl = request.args.get('shareUrl')
    except Exception:
        response = Response(
            json.dumps({
                'message': 'Arguments ERROR',
                'statusCode': 0
            }),
            mimetype='application/json')
    else:
        try:
            isSuccess = instantboxManager.is_rm_container(containerId)
            if not isSuccess:
                raise Exception

        except Exception:
            response = Response(
                json.dumps({
                    'message': 'RM docker containers ERROR',
                    'shareUrl': '',
                    'statusCode': 0,
                }),
                mimetype='application/json')
        else:
            response = Response(
                json.dumps({
                    'message': 'SUCCESS',
                    'statusCode': 1,
                    'containerId': containerId,
                }),
                mimetype='application/json')

    response.headers.add('Server', 'python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route('/v2/superinspire/getOS')
def getOS():
    open_port = None

    try:
        os_name = request.args.get('os')
        if not instantboxManager.is_os_available(os_name):
            raise Exception
    except Exception:
        response = Response(
            json.dumps({
                'message': 'The image is not supported at this time ERROR',
                'statusCode': 0
            }),
            mimetype='application/json')
    else:
        os_mem = request.args.get('mem')
        os_cpu = request.args.get('cpu')
        os_port = request.args.get('port')
        os_timeout = request.args.get('timeout')
        try:
            if os_mem is None:
                os_mem = 512
            elif isinstance(os_mem, str):
                os_mem = int(os_mem)
            else:
                raise Exception
            if os_cpu is None:
                os_cpu = 1
            elif isinstance(os_cpu, str):
                os_cpu = int(os_cpu)
            else:
                raise Exception
        except Exception:
            response = Response(
                json.dumps({
                    'message': 'os_mem or os_cpu argument ERROR',
                    'shareUrl': '',
                    'statusCode': 0,
                }),
                mimetype='application/json')
        else:
            max_timeout = 3600 * 24 + time.time()
            if os_timeout is None:
                os_timeout = max_timeout
            else:
                os_timeout = min(float(os_timeout), max_timeout)
            try:
                container_name = instantboxManager.is_create_container(
                    mem=os_mem,
                    cpu=os_cpu,
                    os_name=os_name,
                    os_timeout=os_timeout,
                    open_port=os_port,
                )
                if container_name is None:
                    raise Exception
                else:
                    ports = instantboxManager.get_container_ports(container_name)
                    if '1588/tcp' in ports:
                        webshell_port = ports['1588/tcp']
                    else:
                        webshell_port = ports[1588]

                    if os_port is not None and SWARM_MODE == True:
                        open_port = ports['{}/tcp'.format(os_port)]
            except Exception:
                response = Response(
                    json.dumps({
                        'message': 'RUN docker containers ERROR',
                        'shareUrl': '',
                        'statusCode': 0,
                    }),
                    mimetype='application/json')
            else:
                response = Response(
                    json.dumps({
                        'message':
                        'SUCCESS',
                        'shareUrl':
                        'http://{}:{}'.format(SERVERURL, webshell_port),
                        'openPort':
                        open_port,
                        'statusCode':
                        1,
                        'containerId':
                        container_name,
                    }),
                    mimetype='application/json')

    response.headers.add('Server', 'python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route('/v2/superinspire/prune')
def pruneTimedoutOS():
    try:
        instantboxManager.remove_timeout_containers()
        response = Response(
            json.dumps({
                'message': 'Success',
                'statusCode': 1
            }),
            mimetype='application/json')
    except Exception:
        response = Response(
            json.dumps({
                'message': 'ERROR',
                'statusCode': 0
            }),
            mimetype='application/json')

    response.headers.add('Server', 'python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=int(65501), debug=False)
