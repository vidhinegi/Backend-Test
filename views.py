# your_app/views.py
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from allauth.account.views import SignupView
from .forms import CustomClientSignupForm

class HomeRedirectView(RedirectView):
    pattern_name = 'home'

def home(request):
    if request.method == 'POST':
        user_type = request.POST.get('user-type')
        if user_type == 'operator':
            return redirect('operator-login')
        elif user_type == 'client':
            return redirect('client-login')
    return render(request, 'home.html')

def operator_login(request):
    if request.method == 'POST':
        username = request.POST.get('operator-username')
        password = request.POST.get('operator-password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse("Operator logged in successfully.")
        else:
            return HttpResponse("Invalid operator credentials.")
    return render(request, 'operator_login.html')

def client_login(request):
    if request.method == 'POST':
        username = request.POST.get('client-username')
        password = request.POST.get('client-password')

        # Authenticate the client
        user = authenticate(request, username=username, password=password)

        if user:
            # Log in the client
            login(request, user)
            return HttpResponse("Client logged in successfully.")
        else:
            return HttpResponse("Invalid client credentials.")

    return render(request, 'client_login.html')

class CustomClientSignupView(SignupView):
    template_name = 'client_signup.html'  # Align with Django-allauth convention
    form_class = CustomClientSignupForm
    
    # You can override other methods as needed
"""

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from .forms import CustomClientSignupForm
from django.views.generic.base import RedirectView

class HomeRedirectView(RedirectView):
    pattern_name = 'home'
    template_name = 'temp/home.html'

def home(request):
    if request.method == 'POST':
        user_type = request.POST.get('user-type')
        if user_type == 'operator':
            return redirect('operator-login')
        elif user_type == 'client':
            return redirect('client-login')
    return render(request, 'home.html')

def operator_login(request):
    if request.method == 'POST':
        username = request.POST.get('operator-username')
        password = request.POST.get('operator-password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse("Operator logged in successfully.")
        else:
            return HttpResponse("Invalid operator credentials.")
    return render(request, 'operator_login.html')

def client_login(request):
    if request.method == 'POST':
        username = request.POST.get('client-username')
        password = request.POST.get('client-password')

        # Authenticate the client
        user = authenticate(request, username=username, password=password)

        if user:
            # Log in the client
            login(request, user)
            return HttpResponse("Client logged in successfully.")
        else:
            return HttpResponse("Invalid client credentials.")

    return render(request, 'client_login.html')

class CustomClientSignupView(SignupView):
    template_name = 'client_signup.html'
    form_class = CustomClientSignupForm
    
def client_signup(request):
    if request.method == 'POST':
        form = CustomClientSignupForm(request.POST)
        if form.is_valid():
            # Assuming you're using django-allauth, use form.save to create the user
            user = form.save(request)
            
            # Log in the user after signup
            login(request, user)

            # Your additional logic after successful signup
            # For example, redirect to the client's dashboard
            return redirect('client-dashboard')
    else:
        form = CustomClientSignupForm()

    return render(request, 'client_signup.html', {'form': form})



"""from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileUploadSerializer

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_file = request.FILES['file']
            file_extension = uploaded_file.name.split('.')[-1].lower()

            allowed_extensions = ['pptx', 'docx', 'xlsx']
            if file_extension not in allowed_extensions:
                return Response({'error': 'Invalid file format'}, status=status.HTTP_400_BAD_REQUEST)

            # Process the file as needed (e.g., save it to storage)
            # For simplicity, let's just print the file name
            print(f"Uploaded file: {uploaded_file.name}")

            return Response({'success': 'File uploaded successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""