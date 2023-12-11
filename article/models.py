from django.db import models
from accounts.models import CustomUser
# Create your models here.



class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
class UserPreferences(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    preference = models.ForeignKey(Categories,on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'preference']]






class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='article_image/',null=True,blank=True)
    tags = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)




class UserInteraction(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    liked=models.BooleanField(default=False)
    disliked=models.BooleanField(default=False)
    blocked=models.BooleanField(default=False)

    def like(self):
        self.liked=True
        self.disliked=False
        self.blocked=False
        self.save()

    def dislike(self):
        self.liked=False
        self.disliked=True
        self.blocked=False
        self.save()

    def block(self):
        self.liked=False
        self.disliked=False
        self.blocked=True
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.article.name} Interaction"





