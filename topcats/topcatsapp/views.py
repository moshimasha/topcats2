from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Recipes
from .models import Groups
from .models import User_Groups

'''
class RecipesDetailView(generic.DetailView):
    model = Recipes
    template_name = 'recipe_detail.html'
    context_object_name = 'recipes'
    recipe = Book.objects.get(pk=primary_key)
'''

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