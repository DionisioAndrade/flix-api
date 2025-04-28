from django.db import models


COUNTRIES = [
    ('BR', 'Brasil'),
    ('US', 'Estados Unidos'),
    ('FR', 'França'),
    ('DE', 'Alemanha'),
    ('IT', 'Itália'),
    ('ES', 'Espanha'),
    ('UK', 'Reino Unido'),
    ('JP', 'Japão'),
    ('KR', 'Coreia do Sul'),
    ('CN', 'China'),
    ('IN', 'Índia'),
    ('RU', 'Rússia'),
    ('AU', 'Austrália'),
    ('MX', 'México'),
    ('AR', 'Argentina'),
    ('CA', 'Canadá'),
]


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=2, choices=COUNTRIES, blank=True, null=True)

    def __str__(self):
        return self.name
