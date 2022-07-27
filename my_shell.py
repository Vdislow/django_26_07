from shop.models import Item, Purchase
from django.utils import timezone

item1 = Item(name='Сonditioner', price=400)
item1.save()
item2 = Item(name='Cold beer', price=2)
item2.save()
item3 = Item(name='Chips', price=2)
item3.save()
item4 = Item(name='4K UHD TV', price=2000)
item4.save()
item5 = Item(name='Sofa', price=300)
item5.save()

item1.purchase_set.create(name='Elsa', age=28, date_purchase=timezone.now())
item1.purchase_set.create(name='Sub', age=44, date_purchase=timezone.now())
item2.purchase_set.create(name='Dominic', age=47, date_purchase=timezone.now())
item2.purchase_set.create(name='Gomer', age=39, date_purchase=timezone.now())
item3.purchase_set.create(name='Leonel', age=35, date_purchase=timezone.now())
item3.purchase_set.create(name='Andrew', age=41, date_purchase=timezone.now())
item4.purchase_set.create(name='Lucas', age=40, date_purchase=timezone.now())
item4.purchase_set.create(name='Liam', age=45, date_purchase=timezone.now())
item5.purchase_set.create(name='Peter', age=37, date_purchase=timezone.now())
item5.purchase_set.create(name='Oleg', age=35, date_purchase=timezone.now())


