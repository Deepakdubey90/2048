from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import game.views

urlpatterns = [
    url(r'^$', game.views.index, name='index'),
    url(r'^do', game.views.do, name='do'),
    url(r'^admin/', include(admin.site.urls)),
]
