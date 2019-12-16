from django import forms
from django.db.models import Count
from django.core.files.storage import default_storage
from .models import Page, Category
from .widgets import FileUploadableTextArea


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


class PageForm(forms.ModelForm):
    """ページの追加フォーム"""

    class Meta:
        model = Page
        fields = '__all__'
        widgets = {
            'text': FileUploadableTextArea,  # このように!
        }


class FileUploadForm(forms.Form):
    """ファイルのアップロードフォーム"""
    file = forms.FileField()

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        file_url = default_storage.url(file_name)
        return file_url
