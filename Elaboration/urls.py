from django.conf.urls import url
import Elaboration.views
urlpatterns = [
    url(r'^save$', Elaboration.views.save_elaboration, name='save'),
    url(r'^submit$', Elaboration.views.submit_elaboration, name='submit'),
]

