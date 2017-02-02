from django.conf.urls import url

from .views import (slides, slide_topics, slide_stack, search, refresh_structure)

urlpatterns = [
    url(r'^$', slides, name='slides'),
    url(r'^search/$', search, name='search'),
    url(r'^refreshstructure/$', refresh_structure, name='refreshstructure'),
    url(r'^(?P<topic>[\w|\s]+)/$', slide_topics, name='slidetopics'),
    url(r'^(?P<topic>[\w|\s]+)/(?P<slug>[\w-]+)/$', slide_stack, name='slidestack'),
]
