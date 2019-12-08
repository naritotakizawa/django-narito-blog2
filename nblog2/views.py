from django.db.models import Q
from django.http import HttpResponseBadRequest, JsonResponse
from django.views import generic
from .forms import FileUploadForm, NoteSearchForm
from .models import Note, Category


class NoteList(generic.ListView):
    model = Note
    paginate_by = 10
    ordering = '-created_at'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = NoteSearchForm(self.request.GET or None)
        if form.is_valid():
            category = form.cleaned_data.get('category')
            if category:
                queryset = queryset.filter(category=category)

            key_word = form.cleaned_data['key_word']
            if key_word:
                queryset = queryset.filter(Q(title__icontains=key_word) | Q(page__text__icontains=key_word)).distinct()

        return queryset.select_related('category')


class NoteDetail(generic.DetailView):
    model = Note


def upload(request):
    """ファイルのアップロード用ビュー"""
    form = FileUploadForm(files=request.FILES)
    if form.is_valid():
        path = form.save()
        url = '{0}://{1}{2}'.format(
            request.scheme,
            request.get_host(),
            path,
        )
        return JsonResponse({'url': url})
    return HttpResponseBadRequest()
