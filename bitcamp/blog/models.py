from pydoc import describe
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=124, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    describtion = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='photo/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    
    def __str__(self) -> str:
        return self.category_name

    