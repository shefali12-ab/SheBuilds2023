from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuesModel(models.Model):
    qno = models.IntegerField(unique=True, null=True)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class DiscussionModel(models.Model):
    TOPICS = (
    ('Mental Wellbeing', 'Mental Wellbeing'),
    ('Physical Health', 'Physical Health'),
    ('Childcare', 'Childcare'),
    ('Other', 'Other')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=300, choices=TOPICS, default='Other')
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.title)
 
class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    discussion  = models.ForeignKey(DiscussionModel,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
 
    def __str__(self):
        return str(self.comment)