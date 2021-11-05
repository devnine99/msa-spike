import json
import os

import django

from consumer_framework.app import ConsumerFramework

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from app.shop.events import ShopCreateEvent, ShopDeleteEvent


app = ConsumerFramework('shop')
app.config(
    bootstrap_servers=['localhost:9092'],
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
