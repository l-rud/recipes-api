from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import RecipeModel
from .serializers import RecipeModelSerializer
from .permissions import ReadOnly, IsAuthenticatedOrReadOnly

class RecipeModelListCreate(generics.ListCreateAPIView):
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Apply custom permission class

class RecipeModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeModelSerializer
    permission_classes = [IsAuthenticated]  # Require authenticated user for detail view