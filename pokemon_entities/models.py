from django.db import models


class Pokemon (models.Model):
    title_ru = models.CharField('название на русском', max_length=200)
    title_en = models.CharField(
        'название на английском',
        max_length=200,
        null=True,
        blank=True
    )
    title_jp = models.CharField(
        'название на японском',
        max_length=200,
        null=True,
        blank=True
    )
    image = models.ImageField(verbose_name='изображение', blank=True, null=True)
    description = models.TextField('описание')
    previous_evolution = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions',
        verbose_name='из кого эволюционировал'
    )

    def __str__(self):
        return self.title_ru

    def img_url(self):
        return self.image.url

    def next_evolution(self):
        if self.next_evolutions.exists():
            return self.next_evolutions.all()[0]
        return None

    def pokemon_id(self):
        return self.id


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,verbose_name='покемон')
    lat = models.FloatField('координата latitude')
    lon = models.FloatField('координата longitude')
    appeared_at = models.DateTimeField('время появления')
    disappeared_at = models.DateTimeField('время исчезания')
    level = models.IntegerField('уровень', null=True, blank=True)
    health = models.IntegerField('здоровье', null=True, blank=True)
    strength = models.IntegerField('сила', null=True, blank=True)
    defence = models.IntegerField('урон', null=True, blank=True)
    stamina = models.IntegerField('выносливость', null=True, blank=True)
