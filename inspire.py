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
    "20000":"CentOS_7",
    "20001":"CentOS_6.10",
    "20002":"CentOS_latest",
    "30000":"2018.12.01",
    "30001":"Arch_latest",
    "40000":"Debian_9.6.0",
    "40001":"Debian_latest",
    "50000":"Fedora_29",
    "50001":"Fedora_28",
    "50002":"Fedora_latest",
}

OS_LIST = {
    "Ubuntu":{
        '12.04':"10000",
        '14.04':"10001", 
        '16.04':"10002", 
        '18.04':"10003",
        'latest':"10004",
        },
    "CentOS":{
        '7':"20000",
        '6.10':"20001",
        'latest':"20002",
        },
    "Arch Linux":{
        "2018.12.01":"30000",
        "latest":"30001",
        },
    "Debian":{
        "9.6.0":"40000",
        "latest":"40001",
        },
    "Fedora":{
        "29":"50000",
        "28":"50001",
        "latest":"50002",
        },

    }


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
            rand_port = randPort()
            rand_string = genString()
            try:
                # 存redis
                subprocess.check_output(
                    "docker run -d -p {0}:30000 --name=\"{5}\" catone/inspire:{1} rtty -I \"{2}\" -h {3} -p {4} -a\
                     -v -s".format(
                        rand_port, 
                        OS_SWITCH[os_info], 
                        rand_string, 
                        SERVERURL, 
                        SERVERPORT, 
                        rand_string,
                        ),
                    shell=True
                )
            except:
                response = Response(
                    json.dumps({
                        "message":"RUN docker containers error", 
                        "shareUrl":"", 
                        "statusCode":0,
                        "containerId":rand_string,
                        }
                    ),
                    mimetype = 'application/json'
                )
            else:
                response = Response(
                    json.dumps({
                        "message":"SUCCESS", 
                        "shareUrl":shareUrl.format(rand_string), 
                        "statusCode":1
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

    app.run(host="0.0.0.0", port=int(65527), debug = False)


