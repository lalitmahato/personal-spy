from django.db import models
import uuid
from product.models import Product

# Create your models here.
class LocationDeviceDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    ip = models.CharField(max_length=1000, null=True)
    os_name = models.CharField(max_length=1000, null=True)
    version = models.CharField(max_length=1000, null=True)
    browser_name = models.CharField(max_length=1000, null=True)
    browser_version = models.CharField(max_length=1000, null=True)
    cpu_name = models.CharField(max_length=1000, null=True)
    resolution = models.CharField(max_length=1000, null=True)
    time_zone = models.CharField(max_length=1000, null=True)
    language = models.CharField(max_length=1000, null=True)
    number_of_cpu_core = models.CharField(max_length=1000, null=True)
    latitude = models.CharField(max_length=1000, null=True)
    longitude = models.CharField(max_length=1000, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class SpyImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='spy/image/%Y/%m/%d/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class SpyMicrophone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    audio = models.FileField(upload_to='spy/audio/%Y/%m/%d/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class SpyVideo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    audio = models.FileField(upload_to='spy/audio/%Y/%m/%d/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
