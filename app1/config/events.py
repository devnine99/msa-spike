import json
import os

import django

from some_app.app import SomeApp

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from app.shop.events import ShopCreateEvent, ShopDeleteEvent


app = SomeApp(
    'shop',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda value: json.loads(value.decode('utf-8')),
    key_deserializer=lambda key: json.loads(key.decode('utf-8')),
)
app.discover_event(
    ShopCreateEvent,
    ShopDeleteEvent,
)


# TODO: bin으로 실행
if __name__ == '__main__':
    app.run()
