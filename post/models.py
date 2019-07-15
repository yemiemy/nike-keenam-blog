from django.db import models
from django.conf import settings 

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
    	verbose_name_plural ='Categories'

    def __str__(self):

        return self.name
        

class Post(models.Model):

    #django will automatically generate forms when we write these codes
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=60) # null=True , blank=True, default='Random Title' #(null=True means: let the user input value; blank=True means the user can't leave the space balnk)
    body = models.TextField()
    
    quote = models.CharField(max_length=500,  default=True, null=True)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    slide_image = models.FileField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', default=True)
    #field = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)
    lifestyle = models.BooleanField(default=False)
    fashion = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    #image = models.ImageField()

    def __str__(self):

        return "{} published on {}".format(self.title,self.published)

class Message(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=60)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return "{} inboxed on {}".format(self.name,self.published)



class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    writer = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=120)
    body = models.TextField()
    
    published = models.DateTimeField(auto_now_add=True) 
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):

        return "{}'s comment published on {}".format(self.writer,self.published)
