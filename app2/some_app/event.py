import abc


class Event(abc.ABC):
    key = None

    def __init__(self, message):
        self.message = message

    @classmethod
    def check_key(cls, key):
        return key == cls.key

    @abc.abstractmethod
    def consume(self):
        pass


class UnKnownEvent(Event):
    def consume(self):
        print('UnKnownEvent!!')
