from app.shop.models import Shop
from some_app.event import Event


class ShopCreateEvent(Event):
    key = 'shop_create'

    def consume(self):
        print(self.message.key)
        print(self.message.value)
        # Shop.objects.create(**value)


class ShopDeleteEvent(Event):
    key = 'shop_delete'

    def consume(self):
        print(self.message.key)
        print(self.message.value)
        # Shop.objects.filter(id=value['id']).delete()
