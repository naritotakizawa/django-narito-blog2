from django import forms
from django.db.models import Count
from .models import Category


class NoteSearchForm(forms.Form):
    """検索フォーム"""
    key_word = forms.CharField(
        label='キーワード',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '検索キーワード'})
    )

    category = forms.ModelChoiceField(
        label='カテゴリ',
        required=False,
        queryset=Category.objects.annotate(post_count=Count('note')).order_by('name'),
        empty_label='全カテゴリ',
        widget=forms.RadioSelect,
    )
