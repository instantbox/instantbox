import docker

class RmContainer(object):


    def __init__(self):

        self.client = docker.from_env()


    def is_rm_container(self, container_id) -> bool : 
        try:
            container = self.client.containers.get(container_id)
        except docker.errors.NotFound:
            return False
        else:
            container.remove(force=True)
            return True


if __name__ == '__main__':
    

    test = RmContainer()
    print(test.is_rm_container("redisInstance"))