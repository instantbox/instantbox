import docker
import os
import random
import string
import time
import json


class InstantboxManager(object):
    CONTAINER_PREFIX = 'instantbox_managed_'
    TIMEOUT_LABEL = 'org.instantbox.variables.EXPIRATION_TIMESTAMP'
    OS_LIST = None
    SWARM_MODE = False

    def __init__(self):
        self.client = docker.from_env()

        if os.environ.get('SWARM_MODE') == '1' :
            self.SWARM_MODE = True

        try:
            with open('manifest.json', 'r') as os_manifest:
                self.OS_LIST = json.load(os_manifest)
        except Exception:
            pass

        if self.OS_LIST is None:
            raise Exception(
                'Could not load manifest.json. ' +
                'Download it from https://get.instantbox.org/manifest.json'
            )

        self.AVAILABLE_OS_LIST = []
        for os_item in self.OS_LIST:
            for ver in os_item['subList']:
                self.AVAILABLE_OS_LIST.append(ver['osCode'])

    def is_create_container(self,
                            mem,
                            cpu,
                            os_name,
                            os_timeout,
                            open_port=None):
        if open_port is None:
            port_dict = {'1588/tcp': None}
        else:
            port_dict = {'1588/tcp': None, '{}/tcp'.format(open_port): None}

        container_name = self.generateContainerName()
        try:
            if self.SWARM_MODE:
                resource_control = docker.types.Resources(
                    cpu_limit=int(cpu),
                    mem_limit=int(mem),
                )
                self.client.services.create(
                    image=os_name,
                    name=container_name,
                    endpoint_spec=docker.types.EndpointSpec(ports={open_port: 1588}),
                    restart_policy=docker.types.RestartPolicy(condition='any'),
                    labels={self.TIMEOUT_LABEL: str.format('{:.0f}', os_timeout)},
                    # resources=resource_control,
                    tty=True,
                )
            else:
                self.client.containers.run(
                    image=os_name,
                    cpu_period=100000,
                    cpu_quota=int('%d0000' % cpu),
                    mem_limit='%sm' % str(mem),
                    name=container_name,
                    ports=port_dict,
                    restart_policy={'Name': 'always'},
                    labels={self.TIMEOUT_LABEL: str.format('{:.0f}', os_timeout)},
                    tty=True,
                    detach=True,
                )
        except KeyboardInterrupt:
            return None
        else:
            return container_name

    def get_container_ports(self, container_name):
        try:
            if self.SWARM_MODE:
                service_name = container_name
                ports = self.client.services.get(
                    service_name).attrs['Endpoint']['Ports']
                return {
                    item['TargetPort']: item['PublishedPort']
                    for item in ports
                }
            else:
                ports = self.client.containers.get(
                    container_name).attrs['NetworkSettings']['Ports']
                return {
                    port: mapped_ports[0]['HostPort']
                    for port, mapped_ports in ports.items()
                }
        except Exception:
            return None

    def remove_timeout_containers(self):
        if self.SWARM_MODE:
            for container in self.client.services.list():
                if container.name.startswith(self.CONTAINER_PREFIX):
                    timeout = container.attrs['Spec']['Labels'][self.TIMEOUT_LABEL]
                    if timeout is not None and float(timeout) < time.time():
                        self.is_rm_container(container.name)
        else:
            for container in self.client.containers.list():
                if container.name.startswith(self.CONTAINER_PREFIX):
                    timeout = container.labels.get(self.TIMEOUT_LABEL)
                    if timeout is not None and float(timeout) < time.time():
                        self.is_rm_container(container.name)

    def is_rm_container(self, container_id) -> bool:
        if self.SWARM_MODE:
            try:
                container = self.client.services.get(container_id)
            except docker.errors.NotFound:
                return True
            else:
                if container.name.startswith(self.CONTAINER_PREFIX):
                    container.remove()
                return True
        else:
            try:
                container = self.client.containers.get(container_id)
            except docker.errors.NotFound:
                return True
            else:
                if container.name.startswith(self.CONTAINER_PREFIX):
                    container.remove(force=True)
                return True

    def is_os_available(self, osCode=None) -> bool:
        return osCode is not None and osCode in self.AVAILABLE_OS_LIST

    def generateContainerName(self) -> str:
        return self.CONTAINER_PREFIX + ''.join(
            random.sample(string.ascii_letters + string.digits, 16))


if __name__ == '__main__':
    test = InstantboxManager()
    container_name = test.is_create_container(4, 0.1,
                                              'instantbox/alpine:latest',
                                              time.time())
    test.get_container_ports(container_name)
    test.remove_timeout_containers()
    test.is_rm_container(container_name)



