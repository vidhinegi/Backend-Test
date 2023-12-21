from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser

class CustomClientSignupForm(SignupForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']  
    def save(self, request):
        
        user = super().save(request)
        
        
        return user