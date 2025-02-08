from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movies


class Review(models.Model):
    movie = models.ForeignKey(
        Movies,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    #quantidade de avaliações
    stars = models.IntegerField(
        validators=[            #As funções de validação servem para restringir o valor minimo e máximo de avaliações por reviews.
            MinValueValidator(0, 'Avaliação não pode ser inferior à 0 estrelas'),
            MaxValueValidator(5, 'Avaliação não pode ser maior à 5 esrtrelas'),
        ]
        )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie.title
