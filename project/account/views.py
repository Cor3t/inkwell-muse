from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .services import AuthService

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        response = AuthService.login(username, password)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data)
            request.session['user_id'] = user_data['user']
            return redirect('profile')
        
    return render(request, 'login.html')

def register_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            response = AuthService.register( 
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                password = form.cleaned_data['password'],
                )
            if response.status_code == 201:
                return redirect('login/')
            
            print(response.json())
    
    return render(request, 'register.html', {'form': form})
