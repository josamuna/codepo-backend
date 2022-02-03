"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# from monitor_engine.views import init_mqtt_listen

# channel_layer = get_channel_layer()
# print("============= GET CHANNLES =====================")
# async_to_sync(channel_layer.group_send)(
#     "chat_room", 
#     {'type':'init_mqtt_listen','content': 'ov3rd0z'}
# )
# mqtt = MqttConsumer()
# mqtt.init_mqtt_listen({'username': 'ov3rd0z',}) init_mqtt_listen
# init_mqtt_listen()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('monitor_engine.urls'))
]
