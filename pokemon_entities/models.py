from django.db import models


class Pokemon (models.Model):
    title_ru = models.CharField('название на русском', max_length=200)
    title_en = models.CharField('название на английском', max_length=200, default='')
    title_jp = models.CharField('название на японском', max_length=200, default='')
    image = models.ImageField(verbose_name='изображение', blank=True, null=True)
    description = models.TextField('описание', null=True)
    previous_evolution = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='child',
        verbose_name='из кого эволюционировал'
    )

    def __str__(self):
        return self.title_ru

    def img_url(self):
        return self.image.url

    def next_evolution(self):
        if self.child.exists():
            return self.child.all()[0]
        return None

    def pokemon_id(self):
        return self.id


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,verbose_name='покемон')
    lat = models.FloatField('координата latitude')
    lon = models.FloatField('координата longitude')
    appeared_at = models.DateTimeField('время появления', default=None)
    disappeared_at = models.DateTimeField('время исчезания', default=None)
    level = models.IntegerField('уровень')
    health = models.IntegerField('здоровье')
    strength = models.IntegerField('сила')
    defence = models.IntegerField('урон')
    stamina = models.IntegerField('выносливость')
