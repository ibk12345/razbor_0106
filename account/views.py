from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class RegistrationView(APIView):
    def post(self, request):
        serializer =RegistrationSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message =" you are done"
            return Response(message)

    


