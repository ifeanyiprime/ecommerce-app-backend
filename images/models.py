from django.db import models

from products.models import Product

class Image(models.Model):
    image_file = models.ImageField(upload_to='product_images', null=False, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="product_images/thumbnails", null=False, blank=True)
    main = models.BooleanField(default=False)