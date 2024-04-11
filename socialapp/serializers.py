from rest_framework.serializers import ModelSerializer
from .models import CustomUser
class ActiveUserSerializer(ModelSerializer):
    class Meta:
       model=CustomUser
       fields='__all__'

  