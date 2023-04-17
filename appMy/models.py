from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(("İsim"), max_length=50)
    image=models.ImageField(("Dizi-Film"), upload_to=None, max_length=None)
    active=models.BooleanField(("Göster"))
    category=models.CharField(("Kategori"), max_length=50)

    def __str__(self):
        return self.name