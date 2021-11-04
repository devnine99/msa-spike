from kafka import KafkaConsumer

from some_app.event import UnDefinedEvent


class SomeApp:
    def __init__(self, topic):
        self.consumer = KafkaConsumer(topic)
        self.event_classes_registry = {}
        # self.event_classes_registry += self.autodiscover_event()

    def run(self):
        print('registered events:')
        for event_class in self.event_classes_registry:
            print(f'- {event_class}')

        for message in self.consumer:
            self.get_event(message).consume()

    def config(self, **kwargs):
        self.consumer.config.update(**kwargs)

    def discover_event(self, *event_classes):
        self.event_classes_registry.update({event_class.key: event_class for event_class in event_classes})

    # def autodiscover_event(self):
    #     # 장고앱에서 Event 클래스를 상속받은 클래스 모두 가져오도록
    #     return []

    def get_event(self, message):
        try:
            return self.event_classes_registry[message.key](message)
        except KeyError:
            return UnDefinedEvent(message)
