from django.db import models

class Contact(models.Model):
    your_email = models.EmailField()
    title = models.TextField()
    message = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title