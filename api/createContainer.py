import docker


class CreateContainer(object):
    def __init__(self):

        self.client = docker.from_env()

    def is_create_container(self,
                            mem,
                            cpu,
                            web_shell_port,
                            container_name,
                            os_name,
                            open_port=None,
                            rand_port=None) -> bool:

        if open_port is None:
            port_dict = {'1588/tcp': str(web_shell_port)}
        else:
            port_dict = {
                '1588/tcp': str(web_shell_port),
                str(open_port) + '/tcp': str(rand_port)
            }

        try:
            self.client.containers.run(
                image=os_name,
                cpu_period=100000,
                cpu_quota=int("%s0000" % cpu),
                mem_limit="%sm" % mem,
                name=container_name,
                ports=port_dict,
                restart_policy={"Name": "always"},
                tty=True,
                detach=True)
        except Exception:
            return False

        else:
            return True


if __name__ == '__main__':
    test = CreateContainer()
    test.is_create_container("512", 1, 32233, "test_container",
                             "instantbox/ubuntu:latest")
