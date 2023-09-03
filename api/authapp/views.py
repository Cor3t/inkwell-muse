from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import UserSerializer, UserTokenSerializer
from django.contrib.auth.hashers import make_password
from django.http import QueryDict

# Registration View.
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    data = request.data.dict()
    
    if request.POST.get('password') is not None:
        data['password'] = make_password(request.POST.get('password'))

    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        token = RefreshToken.for_user(user)
        serializer = UserTokenSerializer({'user':user, 'token': str(token.access_token)})
        return Response(data=serializer.data)
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
