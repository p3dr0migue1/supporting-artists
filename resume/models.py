import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


LANGUAGES = [
    ('en', _(u'English')),
    ('fr', _(u'French')),
    ('ga', _(u'Irish')),
    ('de', _(u'German')),
    ('it', _(u'Italian')),
    ('pl', _(u'Polish')),
    ('pt', _(u'Portuguese')),
]


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


class Language(models.Model):
    artist = models.ManyToManyField('Artist', related_name='language', blank=True, null=True)
    name = models.CharField(max_length=7, choices=LANGUAGES)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
