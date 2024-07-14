from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy
from .views import RecipeListCreate, RecipeRetrieveUpdateDestroy

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroy.as_view(), name='recipe-detail'),
]