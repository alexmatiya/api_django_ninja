from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    created = created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Категории'
        ordering = ['created']

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=250, blank=False)
    category = models.ForeignKey(Category,
                                 blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='notes')
    created = created = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name_plural = 'Заметки'
        ordering = ['-created']

    def __str__(self):
        return self.title
