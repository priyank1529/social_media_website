from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.views.generic import CreateView
from .models import CustomUser 
from .serializers import ActiveUserSerializer
from .forms import UserCreateForm
from django.urls import reverse
# Create your views here.
class Listview(ListAPIView):
    queryset=CustomUser.get_active_users()
    serializer_class=ActiveUserSerializer
class UserCreateView(CreateView):
    form_class=UserCreateForm
    template_name='create_user.html'
    def get_success_url(self):
        return reverse('list')
    