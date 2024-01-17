from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="images")
    image_url = models.CharField(max_length=256)
    alt_text = models.CharField(max_length=50)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="comments")
    guest_name = models.CharField(max_length=20)
    text = models.TextField()
