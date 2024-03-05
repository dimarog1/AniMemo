from django.db import models


class Anime(models.Model):
    russian_title = models.CharField('Russian title', max_length=50, default='')
    english_title = models.CharField('English title', max_length=50, default='')
    poster = models.CharField('Poster ref', max_length=250, default='')
    rating = models.FloatField('Rating')
    anime_type = models.CharField('Type', max_length=50, default='')
    episodes = models.CharField('Episodes', max_length=10, default='')
    status = models.CharField('Status', max_length=50, default='')
    genre = models.CharField('Genre', max_length=50, default='')
    release = models.CharField('Release', max_length=50, default='')
    studio = models.CharField('Studio', max_length=50, default='')
    age_restrictions = models.CharField('Age restrictions', max_length=10, default='')
    duration = models.CharField('Duration', max_length=50, default='')
    description = models.TextField('Description')
    screens = models.JSONField('Screens')
    trailer = models.CharField('Trailer', max_length=250, default='')
    animego = models.CharField('AnimeGo ref', max_length=250, default='')
    source = models.CharField('Source ref', max_length=250, default='')

    def __str__(self):
        return self.russian_title

    # def get_absolute_url(self):
    #     return f'/anime/{self.id}'

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
