from rest_framework import serializers
from .models import Category
from .models import Recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'category_id', 'category', 'title', 'directions', 'ingredients', 'image']
        