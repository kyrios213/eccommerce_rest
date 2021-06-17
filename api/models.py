from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=20, blank=True, null=True)
    pages = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(blank=True, null=True)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']
    
    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField()
    image_url = models.ImageField(blank=True, null=True)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"{self.product_tag} {self.name}"