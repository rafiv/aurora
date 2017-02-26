from django.conf.urls import patterns, url

import Challenge.views

urlpatterns = [
    url(r'^stack$', Challenge.views.stack, name='stack'),
    url(r'^challenge$', Challenge.views.challenge, name='challenge'),
    url(r'^$', Challenge.views.challenges, name='home'),
    url(r'^myreviews$', Challenge.views.my_review, name='myreviews'),
]