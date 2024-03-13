from django.db import models


class AnimeModel(models.Model):
    english_name = models.CharField('English name', max_length=250, default='', null=True)
    russian_name = models.CharField('Russian name', max_length=250, default='', null=True)
    poster = models.CharField('Poster url', max_length=250, default='', null=True)
    rating = models.FloatField('Rating', null=True)
    url = models.CharField('AnimeGo url', max_length=250, default='')
    source = models.CharField('Source url', max_length=250, default='', null=True)

    def __str__(self):
        return self.russian_name

    class Meta:
        verbose_name = 'AnimeModel'
        verbose_name_plural = 'AnimeModels'
