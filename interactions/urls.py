from django.conf.urls import url

from interactions import api


urlpatterns = [
    url(r'^api/interaction$', api.interaction, name='interaction'),
]
