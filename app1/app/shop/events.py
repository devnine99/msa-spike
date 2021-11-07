from consumer_framework.routers import Router

shop_router = Router()


@shop_router.event(topic='shop', key='shop_create')
def test(message):
    print(message.topic)
    print(message.key)
    print(message.value)
