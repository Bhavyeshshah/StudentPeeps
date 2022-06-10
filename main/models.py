from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='tiles', default="")
    brandlogo = models.ImageField(upload_to='tiles', default="")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

    def get_all_brand():
        return Brand.objects.all()    