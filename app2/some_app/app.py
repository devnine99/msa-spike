from kafka import KafkaConsumer

from some_app.event import UnDefinedEvent


class SomeApp:
    def __init__(self, topic):
        self.consumer = KafkaConsumer(topic)
        self.event_classes = {}
        # self.event_classes += self.autodiscover_event()

    def run(self):
        for message in self.consumer:
            self.get_event(message).consume()

    def config(self, **kwargs):
        self.consumer.config.update(**kwargs)

    def discover_event(self, *classes):
        self.event_classes.update({cls.key: cls for cls in classes})

    # def autodiscover_event(self):
    #     # 장고앱에서 Event 클래스를 상속받은 클래스 모두 가져오도록
    #     return []

    def get_event(self, message):
        try:
            return self.event_classes[message.key](message)
        except KeyError:
            return UnDefinedEvent(message)
