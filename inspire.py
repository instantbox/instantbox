import re
import string
import random
import sys
import json
import subprocess
from flask_cors import CORS
from flask import render_template,redirect
from flask import Flask,request,Response,jsonify



app = Flask(__name__)
CORS(app, resources=r'/*')


SERVERURL = '115.238.228.39'
SERVERPORT = '9999'

OS_SWITCH = {
    "10000":"Ubuntu_12.04",
    "10001":"Ubuntu_14.04",
    "10002":"Ubuntu_16.04",
    "10003":"Ubuntu_18.04",
    "10004":"Ubuntu_latest",
    "20000":"CentOS_6.10",
    "20001":"CentOS_7",
    "20002":"CentOS_latest",
    "30000":"2018.12.01",
    "30001":"Arch_latest",
    "40000":"Debian_9.6.0",
    "40001":"Debian_latest",
    "50000":"Fedora_28",
    "50001":"Fedora_29",
    "50002":"Fedora_latest",
}

OS_LIST = [{
    "label": "Ubuntu",
    "value": "Ubuntu",
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
    ]}, 

]


def randPort():
    rand_port = random.randint(1025, 65536)
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

@app.route('/v1/superspire/getOSList')
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


@app.route('/v1/superspire')
def hello():
    return 'hello'


@app.route('/v1/superspire/rmOS')
def rmOS():
    try:
        containerId = request.args.get("containerId")
        timestamp = request.args.get("timestamp")
        shareUrl = request.args.get("shareUrl")
    except:
        response = Response(
            json.dumps({
                "message":"CONTAINERS_ID ERROR", 
                "statusCode":0
                }
            ), 
            mimetype = 'application/json'
        )
    else:
        # 先验一次redis
        try:
            subprocess.check_output("docker rm -f {0}".format(containerId), shell=True)
        except:
            response = Response(
                json.dumps({
                    "message":"RM docker containers error",
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

    response.headers.add('Server','python flask')       
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'            
    return response


@app.route('/v1/superspire/getOS')
def getOS():
    shareUrl = "https://115.238.228.39:9999/#/?id={0}&username=root&password=123456"

    try:
        os_info = request.args.get("os")
    except:
        response = Response(
            json.dumps({
                "message":"OS_INFO ERROR", 
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
                        "message":"OS_SWITCH ERROR", 
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
                os_timeout = 3600*24

            rand_string = genString()
            try:
                # 存redis
                if os_port == None:
                    subprocess.check_output(
                        "docker run -d -m {5}m --cpu-period=100000 --device-write-bps=\"/dev/mapper/centos-root:1mb\" \
                        --cpu-quota={6}0000 --name=\"{4}\" catone/inspire:{0} rtty -I \"{1}\" \
                        -h {2} -p {3} -a -v -s".format(
                            OS_SWITCH[os_info], 
                            rand_string, 
                            SERVERURL, 
                            SERVERPORT, 
                            rand_string,
                            os_mem,
                            os_cpu,

                            ),
                        shell=True
                    )
                else:
                    subprocess.check_output(
                        "docker run -d -p {7}:{8} -m {5}m  --device-write-bps=\"1mb\" \
                        -cpu-quota={6} --name=\"{4}\" catone/inspire:{0} rtty -I \"{1}\" \
                        -h {2} -p {3} -a -v -s".format(
                            OS_SWITCH[os_info], 
                            rand_string, 
                            SERVERURL, 
                            SERVERPORT, 
                            rand_string,
                            os_mem,
                            int(os_cpu),
                            randPort(),
                            os_port,
                            ),
                        shell=True
                    )

            except:
                response = Response(
                    json.dumps({
                        "message":"RUN docker containers error", 
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
                        "shareUrl":shareUrl.format(rand_string), 
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


