from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="post/")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)


    def __str__(self) -> str:
        return self.name

# Create your models here.
