import subprocess
import yaml

try:
    input = raw_input  # Python 2
except NameError:
    pass               # Python 3


def init():
    print("Init inspire...")
    public_ip = input("Please enter your public ip: ")
    public_port = input("Please enter your public port(default 9010): ")
    return public_ip, public_port


def cloneIndex():
    subprocess.check_output("git clone https://github.com/super-inspire/super-inspire-frontend.git /var/", shell=True)


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
        print("init.sh init fail!")


if __name__ == '__main__':
    public_ip, public_port = init()
    modify_yml(public_ip, public_port)
    call_init_docker_compose()
