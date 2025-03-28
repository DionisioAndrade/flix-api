from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField(blank=True, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(blank=True, null=True)    
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['title']   
    