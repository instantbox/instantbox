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

OS_LIST = {
    "Ubuntu":{
        '12.04',
        '14.04', 
        '16.04', 
        '18.04',
        },
    "CentOS":{
        '7',
        '6.10',
        },
    "Arch Linux":{
        "2018.12.01",
        },
    "Debian":{
        "9.6.0",
        },
    "Fedora":{
        "29",
        "28",
        }
    }

OS_SWITCH = {
    "10000":,
    "10001":,
    "10002":,

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

@app.route('/v1')
def hello():
    return 'hello'

@app.route('/v1/superspire/getOS')
def getOS():
    shareUrl = "https://115.238.228.39:9999/#/?id={0}&username=root&password=123456"

    os_info = request.args.get("os")
    try:
        os_name = os_info.split('_')[0]
        os_version = os_info.split('_')[1]
    except:
        response = Response(
            json.dumps(
                {
                    "message":"OS_INFO ERROR", 
                    "statusCode":302
                    }
                ), 
            mimetype = 'application/json'
            )

    else:
        print(os_name)
        print(os_version)
        if os_name not in OS_LIST:
            response = Response(
                json.dumps(
                    {
                        "message":"Not support OS!", 
                        "statusCode":404
                        }
                    ), 
                mimetype = 'application/json'
                )

        else:
            if os_version not in OS_LIST[os_name]:
                response = Response(
                    json.dumps(
                        {
                            "message":"Not support OS_VERSION!", 
                            "statusCode":403
                            }
                        ), 
                    mimetype = 'application/json'
                    )
            
            else:
                print(">>>>")
                rand_port = randPort()
                rand_string = genString()

                subprocess.check_output(
                    "docker run -d -p {0}:30000 catone/inspire:{1}_{2} rtty -I \"{3}\" -h {4} -p {5} -a -v -s".format(
                        rand_port, os_name, os_version, rand_string, SERVERURL, SERVERPORT
                        ),
                    shell=True
                    )
                response = Response(
                    json.dumps(
                        {
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



