from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.http import urlencode
from django.db.models import Q
from webapp.forms import SimpleSearchForm
from webapp.models import File


class IndexView(ListView):
    template_name = 'index.html'
    model = File
    context_object_name = 'files'
    ordering = ['-date']
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class FileDetailView(DetailView):
    context_object_name = 'file'
    model = File
    template_name = 'file_detail.html'


class FileCreateView(CreateView):
    model = File
    template_name = 'add.html'
    fields = ['name', 'file', 'access']

    def form_valid(self, form):
        file = File(
            name = form.cleaned_data['name'],
            author = self.request.user,
            file = form.cleaned_data['file'],
            access= form.cleaned_data['access']
        )
        file.save()
        return redirect('webapp:file_detail', pk=file.pk)

class FileUpdateView(UserPassesTestMixin, UpdateView):
    model = File
    template_name = 'edit.html'
    fields = ['name', 'file', 'access']

    def test_func(self):
        file_pk = self.kwargs.get('pk')
        file = File.objects.get(pk=file_pk)
        return self.request.user == file.author or self.request.user.has_perm('webapp.change_file')

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={"pk": self.object.pk})


class FileDeleteView(UserPassesTestMixin, DeleteView):
    model = File
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        file_pk = self.kwargs.get('pk')
        file = File.objects.get(pk=file_pk)
        return self.request.user == file.author or self.request.user.has_perm('webapp.delete_file')

