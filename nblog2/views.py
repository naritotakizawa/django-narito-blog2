from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.views import generic
from .forms import NoteSearchForm
from .models import Note


class NoteList(generic.ListView):
    model = Note
    queryset = Note.objects.filter(is_public=True)
    paginate_by = 12
    ordering = '-created_at'

    def get_queryset(self):
        self.category = self.key_word = ''
        queryset = super().get_queryset()
        form = self.form = NoteSearchForm(self.request.GET or None)
        if form.is_valid():
            category = self.category = form.cleaned_data.get('category')
            if category:
                queryset = queryset.filter(category=category)

            key_word = self.key_word = form.cleaned_data['key_word']
            if key_word:
                queryset = queryset.filter(Q(title__icontains=key_word) | Q(text__icontains=key_word)).distinct()

        return queryset.select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        heading = ''
        if self.category:
            heading += '「{}」'.format(self.category.name)
        if self.key_word:
            heading += '「{}」'.format(self.key_word)
        if heading:
            heading += 'の検索結果'
        else:
            heading = '全てのノート'
        context['heading'] = heading
        context['search_form'] = self.form
        return context


class PrivateNoteList(LoginRequiredMixin, NoteList):
    queryset = Note.objects.filter(is_public=False)
    raise_exception = True


class NoteDetail(generic.DetailView):
    model = Note

    def get_object(self, queryset=None):
        note = super().get_object()
        if note.is_public or self.request.user.is_authenticated:
            return note
        else:
            raise Http404
