from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField('タイトル', max_length=32)
    thumbnail = models.ImageField('サムネイル')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    is_public = models.BooleanField('公開可能か?', default=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', default=timezone.now)

    def __str__(self):
        return self.title


class Page(models.Model):
    text = models.TextField('本文')
    image = models.ImageField('画像', blank=True)
    book = models.ForeignKey(Note, verbose_name='どのBookのページ?', on_delete=models.CASCADE)
    index = models.PositiveIntegerField('インデックス', default=0)

    class Meta(object):
        ordering = ['index']

    def __str__(self):
        return self.text[:100]
