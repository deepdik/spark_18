from django.conf.urls import include, url

from spark_18.views import api_root

urlpatterns = [
    url(r'^$', api_root, name='api_root'),
    url(r'^', include('spark_18.apps.token_pool.routers')),

]