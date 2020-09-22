import abc


class PlatronClient(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, merchant, secret_key):
        pass

    @abc.abstractmethod
    def request(self, url, params):
        pass
