from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.

class RegisterApi(APIView):

    def post(self,request):
        try:
            data=request.data
            serializer=UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':200,
                    'message':'User Registered Successfully,check email',
                    'data':serializer.data
                })
            return Response({
            'status':400,
            'message':'User Registration Failed',
            'data':serializer.errors
        })
        except Exception as e:
            return Response({
                'status':400,
                'message':'User Registration Failed',
                'data':str(e)
            })