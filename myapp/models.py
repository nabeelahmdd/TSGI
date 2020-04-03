from django.db import models

# Create your models here.
class Notice(models.Model):
    subject = models.CharField(max_length=100)
    mmsg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject