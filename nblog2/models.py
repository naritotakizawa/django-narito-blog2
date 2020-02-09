from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=100)

    def __str__(self):
        if hasattr(self, 'note_count'):
            return f'{self.name}({self.note_count})'
        return self.name


class Note(models.Model):
    title = models.CharField('タイトル', max_length=100)
    thumbnail = models.ImageField('サムネイル')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    text = models.TextField('本文', blank=True)
    is_public = models.BooleanField('公開可能か?', default=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', default=timezone.now)

    def __str__(self):
        return self.title
