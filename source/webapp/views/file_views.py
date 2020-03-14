from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.http import urlencode
from django.db.models import Q
from django.views import View
from webapp.forms import SimpleSearchForm, FileForm, FileAnonymousForm, PrivateForm
from webapp.models import File, Private


class IndexView(ListView):
    template_name = 'index.html'
    model = File
    context_object_name = 'files'
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        context['files'] = File.objects.filter(access='base').order_by('-date')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = PrivateForm()
        file = File.objects.get(pk=self.kwargs['pk'])
        privates = Private.objects.filter(file=file)
        users=[]
        for private in privates:
            users.append(private.user)
        context['users'] = users
        return context


class FileCreateView(CreateView):
    model = File
    template_name = 'add.html'

    def get_form_class(self):
        if self.request.user.is_anonymous:
            self.form_class = FileAnonymousForm
        else:
            self.form_class = FileForm
        return self.form_class

    def form_valid(self, form):
        self.object = form.save(commit=False)
        author = self.request.user
        self.object.author_id = author.pk
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class FileUpdateView(UserPassesTestMixin, UpdateView):
    model = File
    template_name = 'edit.html'

    def get_form_class(self):
        if self.request.user.is_anonymous:
            self.form_class = FileAnonymousForm
        else:
            self.form_class = FileForm
        return self.form_class

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


class AddToPrivate(View):
    template_name = 'add.html'
    model = Private
    form_class = None


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        file = get_object_or_404(File, pk=request.POST.get('pk'))
        self.object = form.save(commit=False)
        user = form.cleaned_data['user']
        print(user, 'yes')
        if user in User.objects.all():
            Private.objects.get_or_create(file=file, user=user)
        return JsonResponse({'pk': file.pk})


class UserPrivateDelete(View):
    def post(self, request):
        file = File.objects.get(pk = int(request.POST['file_id']))
        user = User.objects.get(id = int(request.POST['user_id']))
        Private.objects.filter(file=file, user=user).delete()
        return JsonResponse({'status':'200'})