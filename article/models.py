from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Articles(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    body=models.TextField()
    author=models.ForeignKey('Author', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
