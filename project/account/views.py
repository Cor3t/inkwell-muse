from django.shortcuts import render, redirect
import requests

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        url = "http://127.0.0.1:8000/auth/login/"
        data = {'username': username, 'password':password}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data)
            request.session['user_id'] = user_data['user']
            return redirect('profile')
        
    return render(request, 'login.html')

def register_view(request):
    pass
