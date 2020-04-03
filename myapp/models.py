from django.db import models
from django.db.models.deletion import CASCADE



# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    def __str__(self):
        return self.name


    
class Notice(models.Model):
    subject = models.CharField(max_length=100)
    mmsg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)
    def __str__(self):
        return self.subject