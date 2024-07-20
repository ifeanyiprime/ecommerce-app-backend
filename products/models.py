import uuid
from django.db import models
from accounts.models import CustomUser

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    product_img = models.ImageField(upload_to='products', null=False, blank=True)
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=2000)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

