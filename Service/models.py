from django.db import models
class Service(models.Model):
     Project_title=models.CharField(max_length=10)
     Project_description=models.TextField()
     dates=models.DateField()
     image=models.FileField(upload_to="news/",max_length=250,null=True,default=None)
     Project_status=models.TextField()

