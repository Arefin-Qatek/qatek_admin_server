from django.db import models

class HomePageContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='homepage/images/')

    def __str__(self):
            return self.title