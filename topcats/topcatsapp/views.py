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
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RecipeConvertForm
import requests
import supabase


file_storage = FileStorage()

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(request, username=username, password=password)
        user = supabase.auth.sign_up({ "email":username, "password": password })
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


'''
class RecipesDetailView(generic.DetailView):
    model = Recipes
    template_name = 'recipe_detail.html'
    context_object_name = 'recipes'
    recipe = Book.objects.get(pk=primary_key)
'''

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

'''
def get_recipe_from_site(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = RecipeConvertForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            url = form.cleaned_data['input_url']
            scraper = scrape_me(url)
           # html = requests.get(url).content
            #scraper = scrape_html(html=html, org_url=url)

            print(scraper.ingredients())
            print(scraper.ingredient_groups())
            print(scraper.instructions())
            print(scraper.instructions_list())
            #scraper.yields()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('recipes'))
        
    else:
        form = RecipeConvertForm()

    # If this is a GET (or any other method) create the default form.

    return render(request, 'recipes.html', {'form': form})




class RecipesListView(generic.ListView):
    model = Recipes
    context_object_name = 'recipes_list'
    template_name = 'recipes.html'
    queryset = Recipes.objects.all()

    def get_queryset(self):
        return (
            Recipes.objects.all()
        )

class GroupsListView(generic.ListView):
    model = Groups
    context_object_name = 'groups_list'
    template_name = 'groups.html'

    def get_queryset(self):
        group_ids = User_Groups.objects.filter(userid=self.request.user)
        groups = Groups.objects.filter(pk__in=group_ids)
        return groups

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
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
            file_storage.save(file.name, file)
            return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LoadView(APIView):
    def get(self, request, *args, **kwargs):
        #print(file_storage.listall())
        return Response(file_storage.listall())

class LearnView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            file_name = request.data['file']
            file = file_storage.open(file_name)
            # Save the file or handle it as needed
            response = FileResponse(file, as_attachment=True, filename=file_name)
            return response
        except FileNotFoundError:
            raise Http404("File not found")
'''
def recipe_detail_view(request, pk):
    try:
        recipes = Recipes.objects.get(pk=pk)
    except Recipes.DoesNotExist:
        raise Http404('Book does not exist')
    return render(request, 'recipe_detail.html', context={'recipes': recipes})

def home(request):
    return render(request, 'index.html')

def groups(request):
    return render(request, 'groups.html')
'''