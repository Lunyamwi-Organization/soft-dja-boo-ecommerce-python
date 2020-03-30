from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    #all my category images will be uploaded to the category folder
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('products_by_category', args = [self.slug])
    def __str__(self):
        return self.name

class Product(models.Model):
     name = models.CharField(max_length=250, unique=True)
     slug = models.SlugField(max_length=250, unique=True )
     description = models.TextField(blank=True)
     category = models.ForeignKey(Category, on_delete =models.CASCADE)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     image = models.ImageField(upload_to='product', blank=True)
     #all my product images will be uploaded to the product folder
     stock = models.IntegerField()
     available = models.BooleanField(default=True)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)
     #created and updated for when these happened to the product fields will be automatically updated
     class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
     def get_url(self):
        #the first is the category slug, the second is the product slug
        return reverse('product_detail', args = [self.category.slug, self.slug])
     def __str__(self):
        return self.name