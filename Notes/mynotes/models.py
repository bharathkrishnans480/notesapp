from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=120,null=True)
    description = models.CharField(max_length=230)
    image = models.ImageField(upload_to="notesimages",null=True,blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


