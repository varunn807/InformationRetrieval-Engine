from django.urls import path

from . import views
app_name = 'IRapp'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('result', views.index, name='index'),
    path('test', views.test, name='test'),

]