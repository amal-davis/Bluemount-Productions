from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField()

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title
    


class CareerPosition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name