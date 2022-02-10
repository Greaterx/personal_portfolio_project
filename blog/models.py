from django.db import models

class my_blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now=False)

    def __str__(self):
        return self.title
