"""Posts Models."""

# Django
from django.db import models


class Post(models.Model):
    """Post model."""

    profile_id = models.ForeignKey('users.Profile',on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return '{} by @{}'.format(self.title, self.profile_id.user.username)