import docker

class CreateContainer(object):



    def __init__(self):

        self.client = docker.from_env()


    def is_create_container(self, mem, cpu, web_shell_port, container_name, os_name, open_port=None, rand_port=None) -> bool : 
        
        shell = "bash"

        if "alpine" in os_name:
            shell = "sh"

        if open_port == None:
            port_dict = {str(web_shell_port)+'/tcp':str(web_shell_port)}
        else:
            port_dict = {str(web_shell_port)+'/tcp':str(web_shell_port),
                str(rand_port)+'/tcp':str(open_port)
            }

        try:

            self.client.containers.run(
                image="catone/inspire:%s"%os_name,
                command="ttyd_linux.x86_64 -p %s %s -x"%(web_shell_port, shell),
                cpu_period=100000,
                cpu_quota=int("%s0000"%cpu),
                mem_limit="%sm"%mem,
                name=container_name,
                ports=port_dict,
                restart_policy={"Name": "always"},
                tty=True,
                detach=True
                )
        except:
            return False

        else:
            return True


if __name__ == '__main__':
    test = CreateContainer()
    test.is_create_container("512", 1, 32233, "kldasf", "ubuntu16_04")

