from django.db import models
from django.contrib.postgres.fields import JSONField


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    price = models.FloatField()
    features = JSONField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    # category = db.relationship('Category', backref=db.backref('products'), lazy=True)
    # photos = db.relationship('Media', backref=db.backref('product'))

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Media(models.Model):
    image = models.ImageField(upload_to='images/products/')
    is_main = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return 'Photo'
