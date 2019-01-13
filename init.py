import yaml
import subprocess

def is_python_2():
    import sys

    return sys.version_info < (3, 0):


def init():
    if is_python_2() == True:
        print 'Init inspire...'
        public_ip = raw_input("Please enter your public ip: ")
        public_port = raw_input("Please enter your public port(default 9010): ")

    else:
        print("Init inspire...")
        public_ip = input("Please enter your public ip: ")
        public_port = input("Please enter your public port(default 9010): ")

    return public_ip, public_port

def modify_yml(public_ip, public_port):
    with open("./docker-compose.yml", "r") as yaml_file:

        yaml_obj = yaml.safe_load(yaml_file.read())
        yaml_obj["services"]["inspire"]["environment"]["SERVERURL"] = public_ip
        yaml_obj["services"]["nginx"]["ports"] = {int(public_port):80}


    with open("./docker-compose.yml", "w") as yaml_file:

        yaml.dump(yaml_obj, yaml_file)

def call_init_docker_compose():
    try:
        subprocess.check_output("chmod +x ./init.sh", shell=True)
        subprocess.check_output("./init.sh", shell=True)
    except:
        if is_python_2():
            print 'init.sh init fail!'
        else:
            print("init.sh init fail!")


if __name__ == '__main__':

    public_ip, public_port = init()
    modify_yml(public_ip, public_port)
    call_init_docker_compose()