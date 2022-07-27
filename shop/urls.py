from django.urls import path
from .views import *


urlpatterns = [
    path('', list_item, name='list_item'),
    path('<int:item_id>', detail_item, name='detail_item'),
    path('greetings/', greetings),
]