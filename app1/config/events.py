import json
import os

import django

from consumer_framework import ConsumerFramework

from app.shop.events import shop_router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


app = ConsumerFramework()
app.config(
    bootstrap_servers=['127.0.0.1:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda value: json.loads(value.decode('utf-8')),
    key_deserializer=lambda key: json.loads(key.decode('utf-8')),
)
app.include_router(shop_router)


@app.event(topic='shop', key='shop_create2')
def test(message):
    print(message.topic)
    print(message.key)
    print(message.value)
