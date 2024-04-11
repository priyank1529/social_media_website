from django.urls import path 
from .views import Listview,UserCreateView
urlpatterns=[
    path('',Listview.as_view(),name="list"),
    path('create_user',UserCreateView.as_view(),name="create"),
    
]
