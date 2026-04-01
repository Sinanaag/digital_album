from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    description = models.TextField(blank=True)

    # Optional passkey — if set, users must enter it to see the photos
    # blank=True means you don't HAVE to set a passkey (album is open if empty)
    passkey = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)