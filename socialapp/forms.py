from typing import Any
from .models import CustomUser
from django import forms
from .models import CustomUser

class UserCreateForm(forms.ModelForm):
    retype_password=forms.CharField(label="Retype Password", widget=forms.PasswordInput)
    class Meta:
        model=CustomUser
        fields=['email','username','password','retype_password']
    def clean(self):
          cleaned_data = super().clean()
          password = cleaned_data.get("password")
          retype_password=cleaned_data.get("retype_password")
          username=cleaned_data.get("username")
          existed_user=CustomUser.objects.all().values_list('username')
          if username in existed_user:
              raise forms.ValidationError(
                   "Username is already exist! "
              )
          
          if password != retype_password:
               raise forms.ValidationError(
                "Password and retype password do not match"
            )
          return cleaned_data

        
        

