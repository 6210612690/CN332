from django.db import models
from users.models import User
# Create your models here.

class ProjectBefore (models.Model):

    ProID = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100 ,default='Unapprove')
    projectname = models.CharField(max_length=150)
    projectmanager= models.CharField(max_length=150)
    article = models.CharField(max_length=1500)
    PreStudentID = models.ManyToManyField(User, blank=True, related_name="PreStudentID")
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class ProjectAfter (models.Model):

    CATEGORY = [
        ('OnGoing', 'OnGoing'),
        ('Complete', 'Complete'),
        ]

    ProID = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100 ,default='OnGoing')
    projectname = models.CharField(max_length=150)
    projectmanager= models.CharField(max_length=150)
    article = models.CharField(max_length=1500)
    StudentID = models.ManyToManyField(User, blank=True, related_name="StudentID")
    TeacherID = models.ManyToManyField(User, blank=True, related_name="TeacherID")
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Comment (models.Model):

    projectcommented = models.ManyToManyField(ProjectAfter, blank=True, related_name="projectcommented")
    comment_text = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)

