from django.db import models
from django.utils.html import mark_safe


class Organization(models.Model):
    """
    Модель организации.
    """

    title = models.CharField(max_length=100, verbose_name='Наименование организации')
    description = models.CharField(max_length=500, verbose_name='Описание организации')
    address = models.CharField(max_length=100, verbose_name='Адрес организации')
    postcode = models.IntegerField(verbose_name='Почтовый индекс организации')

    class Meta:
        ordering = ['id']
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    Модель мероприятия.
    """

    title = models.CharField(max_length=100, verbose_name='Наименование мероприятия')
    description = models.CharField(max_length=500, verbose_name='Описание мероприятия')
    organization = models.ManyToManyField(
        Organization, verbose_name='Организующая мероприятие организация'
    )
    image = models.ImageField(
        upload_to='events/', blank=True, null=True, verbose_name='Изображение мероприятия'
    )
    date = models.DateField(verbose_name='Дата мероприятия')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""
