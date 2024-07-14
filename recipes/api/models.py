from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Recipe(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    directions = models.CharField(max_length=2048)
    ingredients = models.CharField(max_length=1024)
    image = models.CharField(max_length=1024)

    def __str__(self):
        return self.title
