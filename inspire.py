import re
import os
import sys
import json
import time
import random
import string
import subprocess
from flask_cors import CORS
from API.redisCli import ConnectRedis
from API.rmContainer import RmContainer
from flask import render_template,redirect
from API.createContainer import CreateContainer
from flask import Flask,request,Response,jsonify



app = Flask(__name__)
CORS(app, resources=r'/*')


redisCli = ConnectRedis()
create_container_client = CreateContainer()
rm_container_client = RmContainer()


SERVERURL = os.popen('curl ip.sb').readlines()[0].split('\n')[0]


OS_SWITCH = {
    "10000":"ubuntu12_04",
    "10001":"ubuntu14_04",
    "10002":"ubuntu16_04",
    "10003":"ubuntu18_04",
    "10004":"ubuntuLatest",
    "20000":"centos6_10",
    "20001":"centos7",
    "20002":"centosLatest",
    "30000":"2018.12.01",
    "30001":"archLatest",
    "40000":"debian9_6_0",
    "40001":"debianLatest",
    "50000":"fedora28",
    "50001":"fedora29",
    "50002":"fedoraLatest",
    "60000":"alpineLatest"
}



OS_LIST = [{
    "label": "Ubuntu",
    "value": "Ubuntu",
    "logoUrl":"http://"+SERVERURL+":9010/icon/ubuntu.png",
    "subList":[{
        'label':"12.04",
        'osCode':"10000"
        }, {
        'label':"14.04",
        'osCode':"10001"
        }, {
        'label':"16.04",
        'osCode':"10002"
        }, {
        'label':"18.04",
        'osCode':"10003"
        }, {
        'label':"latest",
        'osCode':"10004"
        }
    ]}, {
    "label": "CentOS",
    "value": "CentOS",
    "logoUrl":"http://"+SERVERURL+":9010/icon/cent-os.png",
    "subList":[{
        'label':"6.10",
        'osCode':"20000"
        }, {
        'label':"7",
        'osCode':"20001"
        }, {
        'label':"latest",
        'osCode':"20002"
        }
    ]}, {

    "label": "Arch Linux",
    "value": "Arch Linux",
    "logoUrl":"http://"+SERVERURL+":9010/icon/arch.png",
    "subList":[{
        'label':"2018.12.01",
        'osCode':"30000"
        }, {
        'label':"latest",
        'osCode':"30001"
        }
    ]}, {

    "label": "Debian",
    "value": "Debian",
    "logoUrl":"http://"+SERVERURL+":9010/icon/debain.png",
    "subList":[{
        'label':"9.6.0",
        'osCode':"40000"
        }, {
        'label':"latest",
        'osCode':"40001"
        },
    ]}, {

    "label": "Fedora",
    "value": "Fedora",
    "logoUrl":"http://"+SERVERURL+":9010/icon/fedora.png",
    "subList":[{
        'label':"28",
        'osCode':"50000"
        }, {
        'label':"29",
        'osCode':"50001"
        }, {
        'label':"latest",
        'osCode':"50002"
        },
    ]}, {

    "label": "Alpine",
    "value": "Alpine",
    "logoUrl":"http://"+SERVERURL+":9010/icon/alpine.png",
    "subList":[{
        'label':"latest",
        'osCode':"60000"
        },
    ]},

]


def randPort():
    rand_port = random.randint(1, 65536)
    if (6000 <= rand_port <= 7000) or (rand_port == 22):
        randPort()
    else:
        try:
            subprocess.check_output("lsof -i:%s"%(rand_port), shell=True)
        except subprocess.CalledProcessError:
            return rand_port
        else:
            randPort()


def genString():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return salt


@app.route('/v2/superinspire/getOSList')
def returnList():

    response = Response(
        json.dumps(
            OS_LIST
        ),
        mimetype = 'application/json'
    )

    response.headers.add('Server','python flask')
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
    except:
        response = Response(
            json.dumps({
                "message":"Arguments ERROR",
                "statusCode":0
                }
            ),
            mimetype = 'application/json'
        )
    else:
        if redisCli.is_container(containerId):
            try:
                isSuccess = rm_container_client.is_rm_container(containerId)
                if isSuccess != True:
                    raise Exception

            except Exception:
                response = Response(
                    json.dumps({
                        "message":"RM docker containers ERROR",
                        "shareUrl":"",
                        "statusCode":0,
                        }
                    ),
                    mimetype = 'application/json'
                )
            else:
                response = Response(
                    json.dumps({
                        "message":"SUCCESS",
                        "statusCode":1,
                        "containerId":containerId,
                        }
                    ),
                    mimetype = 'application/json'
                )
        else:
            response = Response(
                json.dumps({
                    "message":"docker containers not exist ERROR",
                    "statusCode":0,
                    "containerId":containerId,
                    }
                ),
                mimetype = 'application/json'
            )


    response.headers.add('Server','python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route('/v2/superinspire/getOS')
def getOS():

    shareUrl = "http://{0}:{1}"
    openPort = ''

    try:
        os_info = request.args.get("os")
    except:
        response = Response(
            json.dumps({
                "message":"OS Arguments ERROR",
                "statusCode":0
                }
            ),
            mimetype = 'application/json'
        )
    else:
        try:
            os_mem = request.args.get("mem")
            os_cpu = request.args.get("cpu")
            os_port = request.args.get("port")
            os_timeout = request.args.get("timeout")
        except:
            if os_info not in OS_SWITCH:
                response = Response(
                    json.dumps({
                        "message":"The image is not supported at this time ERROR",
                        "statusCode":0
                        }
                    ),
                    mimetype = 'application/json'
                )
        else:

            if os_mem == None:
                os_mem = 512
            if os_cpu == None:
                os_cpu = 1
            if os_timeout:
                os_timeout = 3600*24+time.time()

            rand_string = genString()
            webShellPort = randPort()
            try:
                if os_port == None:
                    isSuccess = create_container_client.is_create_container(
                        mem=os_mem,
                        cpu=os_cpu,
                        web_shell_port=webShellPort,
                        container_name=rand_string,
                        os_name=OS_SWITCH[os_info],
                        )

                else:
                    openPort = randPort()
                    isSuccess = create_container_client.is_create_container(
                        mem=os_mem,
                        cpu=os_cpu,
                        web_shell_port=webShellPort,
                        container_name=rand_string,
                        os_name=OS_SWITCH[os_info],
                        open_port=os_port,
                        rand_port=openPort
                        )

                if isSuccess != True:
                    raise Exception
            except Exception:
                response = Response(
                    json.dumps({
                        "message":"RUN docker containers ERROR",
                        "shareUrl":"",
                        "statusCode":0,
                        }
                    ),
                    mimetype = 'application/json'
                )
            else:
                redisCli.set_container(rand_string)

                response = Response(
                    json.dumps({
                        "message":"SUCCESS",
                        "shareUrl":shareUrl.format(SERVERURL, webShellPort),
                        "openPort":openPort,
                        "statusCode":1,
                        "containerId":rand_string,
                        }
                    ),
                    mimetype = 'application/json'
                )

    response.headers.add('Server','python flask')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response








if __name__ == '__main__':

    app.run(host="0.0.0.0", port=int(65501), debug = False)


