from django.db import models
from django.utils import timezone
from accounts.models import Account



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


class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=124)
    description = models.CharField(max_length=244)
    text = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='images/post')
    create_date = models.DateTimeField(default=timezone.now())
