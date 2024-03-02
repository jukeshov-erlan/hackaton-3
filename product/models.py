from django.db import models
from slugify import slugify


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, blank=True, primary_key=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(max_length=40, unique=True, blank=True, primary_key=True)
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    body = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product_img/', verbose_name='Картинка', blank=True)
    in_stock = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()



