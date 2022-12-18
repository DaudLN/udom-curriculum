from django.db import models
from django.urls import reverse
from .colleges import *
from .programs import *


class Program(models.Model):

    name = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            unique=True)
    college = models.CharField(max_length=255,
                               null=False,
                               blank=False,
                               choices=college_choices,
                               default=CHAS)
    description = models.TextField(null=True, blank=True)
    years_of_study = models.SmallIntegerField()
    fee = models.PositiveIntegerField()
    knowledge = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    competences = models.TextField(null=True, blank=True)
    special_requirements = models.TextField(null=True, blank=True)
    fields_of_work = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('program_detail', kwargs={'slug': self.slug})
