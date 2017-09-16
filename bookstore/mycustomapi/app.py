from django.conf.urls import url

from mycustomapi.views import root, product, category

from vanilla.mycustomapi.app import MyRESTApiApplication as _MyRESTApiApplication


class MyRESTApiApplication(_MyRESTApiApplication):
    pass

application = MyRESTApiApplication()
