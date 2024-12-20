from django.db import models

# Create your models here.
class Path(models.Model):
    name =  models.CharField(max_length=150)
    time =  models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
