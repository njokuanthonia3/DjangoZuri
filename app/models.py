from django.db import models
from django.urls import reverse # new
from django.utils import timezone
class Post(models. Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()
  


    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        # new
        return reverse('post_detail' , args=[str(self. id)])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments',) # new

    comment = models.CharField(max_length=140)
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default= False)

    def approve(self):
        self.approved_comment = True
        self.save()

   
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.comment




  