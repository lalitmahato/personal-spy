from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    name = models.CharField(max_length=100, null=True)
    product_for = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=1000, null=True)
    price = models.FloatField(null=True)
    thumbnail = models.ImageField(upload_to='product/thumbnail/image', null=True)
    status = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductSlider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    sliding_image = models.ImageField(upload_to='product/slider/image', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
