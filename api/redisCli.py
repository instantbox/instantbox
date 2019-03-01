import redis


class ConnectRedis(object):
    def __init__(self):

        redisPool = redis.ConnectionPool(host="redis", port=6379, db=0)
        self.redisCli = redis.StrictRedis(connection_pool=redisPool)

    def set_value(self, key: str, value: str) -> bool:

        if key is not None or key != '':

            self.redisCli.set(key, value)

            return True
        else:
            return False

    def get_value(self, key: str) -> str:

        result = self.redisCli.get(key)
        if result is not None:
            return result.decode()
        else:
            return None

    def is_container(self, containerId: str) -> bool:

        result = self.redisCli.get(containerId)
        if result is not None:
            return True
        else:
            return False

    def set_container(self, containerId: str) -> bool:

        result = self.redisCli.set(containerId, containerId)
        if result is not None:
            return True
        else:
            return False


if __name__ == '__main__':

    test = ConnectRedis()
    test.set_value("name", "Yuefeng Zhu")
    print(test.get_value("name"))
