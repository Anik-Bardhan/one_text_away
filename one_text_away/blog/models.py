from django.db import models

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    intro=models.TextField()
    body=models.TextField()
    date_add=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_add']

class Comment(models.Model):
    post=models.ForeignKey(Posts,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['date_add']