import requests
class AuthService:
    url = "http://127.0.0.1:8000/auth/"

    def login(username : str, password : str):
        data = {'username': username, 'password':password}
        try:
            response = requests.post(AuthService.url + 'login/', data=data)
            return response
        except:
            return None
    
    def register(**kwargs):
        try:
            response = requests.post(AuthService.url + 'register/', data=kwargs)
            return response
        except:
            return None
    


        