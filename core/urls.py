
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # path('',index.as_view(),name='index'),
    path('', views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
]