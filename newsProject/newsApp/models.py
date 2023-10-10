from django.db import models
from datetime import datetime
from django.urls import reverse


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Описание")
    source = models.CharField("Источник", max_length=50)
    postDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    # upd
    def get_absolute_url(self):
        return reverse("postDetail", args=[self.pk])

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
