from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default="", blank=True, null=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(default="100")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.product.stock_quantity < self.quantity:
            raise ValueError("Insufficient stock")
        
        self.product.stock_quantity -= self.quantity
        self.product.save()
        
        super().save(*args, **kwargs)

    def total_price(self):
        return self.product.price * self.quantity
