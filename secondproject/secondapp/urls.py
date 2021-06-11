from django.conf.urls import url
from secondapp import views
from django.urls import include, path

urlpatterns=[
    path('',views.user,name='user')
]
