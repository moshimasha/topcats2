from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("groups/", views.GroupsListView.as_view(), name="groups"),
    path('recipes/', views.RecipesListView.as_view(), name='recipes'),
    path('recipe/<int:pk>', views.recipe_detail_view, name='recipe-detail'),
]

