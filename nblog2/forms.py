from django import forms
from django.db.models import Count
from .models import Category, Note


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
        queryset=Category.objects.annotate(note_count=Count('note')).order_by('name'),
        widget=forms.RadioSelect,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        all_note_count = Note.objects.filter(is_public=True).count()
        self.fields['category'].empty_label = f'全カテゴリ({all_note_count})'