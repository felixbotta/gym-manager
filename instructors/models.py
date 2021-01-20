from django.db import models
from django.utils import timezone


class Instructor(models.Model):
    url = models.URLField('URL', max_length=200)
    name = models.CharField('Instrutor', max_length=100)
    age = models.DateField('Data de Nascimento')

    gender = (
        (None, 'Escolha seu Gênero'),
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    gender = models.CharField('Gênero', max_length=10, choices=gender)

    services = models.TextField('Acompanhamento')

    created_at = timezone.now().date()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Instrutor'
        verbose_name_plural = 'Instrutores'
