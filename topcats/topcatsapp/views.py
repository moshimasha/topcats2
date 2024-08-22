from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import FileUploadSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .storage import FileStorage
from .groqchain import GroqChain
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RecipeConvertForm
import requests
import supabase

import json

from pypdf import PdfReader


file_storage = FileStorage()
groq_chain = GroqChain()


class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(f"Received username: {username} (type: {type(username)})")
        print(f"Received password: {password} (type: {type(password)})")
        user = file_storage.supabase.auth.sign_in_with_password({ "email":username, "password": password })   
        userpath = file_storage.supabase.auth.get_session().user.id
        request.session['user_id'] = userpath
        return Response({})

class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        print(request)
        data = json.loads(request.body)
        
        username = data.get('username')
        password = data.get('password')
        
        print(f"Received username: {username} (type: {type(username)})")
        print(f"Received password: {password} (type: {type(password)})")
        
        user = file_storage.supabase.auth.sign_up({ "email":username, "password": password })   

        return Response({})


@api_view(['GET'])
def initial(request):
    return Response({})


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file = request.data['file']
            # Save the file or handle it as needed
            user_id = request.session['user_id']
            
            file_storage.save(file.name, file, user_id)
            return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LoadView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        print(user_id)
        return Response(file_storage.listall(user_id))

class LearnView(APIView):
    def get(self, request, file_name):
        try:
            user_id = request.session.get('user_id')
            print(user_id)
            file = file_storage.open(file_name, user_id)
            # Save the file or handle it as needed
            response = FileResponse(file, content_type='application/pdf')
            
            return response
        except FileNotFoundError:
            raise Http404("File not found")
        
class RecallView(APIView):
    def get(self, request):
        #send text data
        user_id = request.session.get('user_id')
        file = file_storage.open(request.GET.get('file_name'), user_id)
        reader = PdfReader(file)
        page = reader.pages[int(request.GET.get('page_no'))]
        return Response(groq_chain.generateQuestions(page.extract_text(), request.GET.get('num_questions')))
    