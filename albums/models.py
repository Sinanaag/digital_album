from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)