import uuid
from django.db import models


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    stage_name = models.CharField(max_length=100, blank=True)  # (optional)
    email = models.EmailField(max_length=254, blank=False, unique=True)  # (uniqueness)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    telephone_number = models.CharField(max_length=11, blank=True)  # (optional)
    biography = models.TextField(blank=True)  # (optional)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'
