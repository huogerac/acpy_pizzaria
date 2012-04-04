from django.conf.urls import patterns, include, url

from .views import hora_atual

urlpatterns = patterns('',

    url(r'hora$', hora_atual, name='hora'),

)
