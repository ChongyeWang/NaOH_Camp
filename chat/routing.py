from django.urls import re_path

from . import consumers, consumers_main

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/chat/', consumers_main.ChatConsumerMain),
]
