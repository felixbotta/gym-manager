from django.db import models
from instructors.models import Instructor
from django.utils import timezone


class Member(models.Model):
    url = models.URLField('URL', max_length=200)
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    birth = models.DateField('Data de Nascimento')

    instructor = models.ForeignKey(Instructor, verbose_name='Instrutor', related_name='member', on_delete=models.CASCADE)

    gender = (
        (None, 'Escolha seu Gênero'),
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    gender = models.CharField('Gênero', max_length=10, choices=gender)

    weight = models.FloatField('Peso')
    height = models.FloatField('Altura')

    created_at = timezone.now().date()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'