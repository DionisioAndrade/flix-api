from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0,'Evaluation cannot be performed if the value is below 0.'),
            MaxValueValidator(5,'The maximum value for evaluation is 5.')
        ]
    )
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.movie.title} - {self.stars} Stars"