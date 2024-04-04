from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
    

class Embed(models.Model):
    embed_code = models.CharField(max_length = 100)

    def __str__(self):
        return self.embed_code

class Video(models.Model):

    embed = models.ForeignKey(Embed, on_delete=models.SET_NULL, null=True, blank=True)  

    title = models.CharField(max_length = 200)
    detail = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.body[0:50]
    



    

    






