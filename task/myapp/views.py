from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import permissions 

def get_tokens_for_user(user):

    ''' THIS FUNCTION PROVIDE TOKEN CREATE MANUALLY '''

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class Registrationview(APIView):
    serializer_class = Registrationserializer
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Registersucsesfull"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class loginview(APIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        email = serializer.initial_data.get('email')
        password = serializer.initial_data.get('password')
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'message': "The User is not registered "}, status=status.HTTP_403_FORBIDDEN)
        if user.email==email:
            if user.password==password:
                token = get_tokens_for_user(user)
                return Response({'id': str(user.id),'token':token,'message':'login success'},status=status.HTTP_200_OK)
            else:
                return response.Response({'errors':'Email or Password is not valid'}, status=status.HTTP_404_NOT_FOUND)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefreshAccessToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Please provide a refresh token'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh_token = RefreshToken(refresh_token)
            access_token = str(refresh_token.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)