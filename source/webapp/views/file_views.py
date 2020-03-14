from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import File


class IndexView(ListView):
    template_name = 'index.html'
    model = File
    context_object_name = 'files'
    ordering = ['-date']
    paginate_by = 10
    paginate_orphans = 1


class FileDetailView(DetailView):
    context_object_name = 'file'
    model = File
    template_name = 'file_detail.html'


# class TaskCreateView(PermissionRequiredMixin, SessionStatMixin, CreateView):
#     model = Task
#     template_name = 'task/create.html'
#     form_class = TaskForm
#     permission_required = 'webapp.add_task'
#     permission_denied_message = 'Access is denied!'

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.created_by = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self):
#         return reverse('webapp:task_view', kwargs={'pk': self.object.pk})

#     def get_form(self, form_class=None):
#         form = super().get_form()
#         user_projects_list = Team.objects.filter(user__username=self.request.user).values_list('project', flat=None)
#         form.fields['project'].queryset = Project.objects.filter(pk__in=user_projects_list)
#         return form

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         users_list = Team.objects.filter(user__username=self.request.user).values_list('user', flat=None)
#         kwargs['users_list'] = users_list
#         return kwargs


# class TaskProjectCreateView(PermissionRequiredMixin, SessionStatMixin, CreateView):
#     template_name = 'task/task_project_create.html'
#     form_class = ProjectTaskForm
#     permission_required = 'webapp.add_task'
#     permission_denied_message = 'Access is denied!'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         project = Project.objects.get(pk=self.kwargs['pk'])
#         context['project'] = project
#         return context

#     def form_valid(self, form):
#         project_pk = self.kwargs.get('pk')
#         project = get_object_or_404(Project, pk=project_pk)
#         project.tasks.create(created_by = self.request.user, **form.cleaned_data)
#         return redirect('webapp:project_view', pk=project_pk)

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         project = self.kwargs['pk']
#         users_in_project = User.objects.filter(user_team__project=project)
#         kwargs['users'] = users_in_project
#         return kwargs

# class TaskUpdateView(PermissionRequiredMixin, UserPassesTestMixin, SessionStatMixin, UpdateView):
#     model = Task
#     template_name = 'task/update.html'
#     form_class = TaskForm
#     context_object_name = 'task'
#     permission_required = 'webapp.change_task'
#     permission_denied_message = 'Access is denied!'

#     def get_success_url(self):
#         return reverse('webapp:task_view', kwargs={'pk': self.object.pk})

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         users_list = Team.objects.filter(user__username=self.request.user).values_list('user', flat=None)
#         kwargs['users_list'] = users_list
#         return kwargs


#     def test_func(self, **kwargs):
#         task = Task.objects.get(pk=self.kwargs.get('pk'))
#         project = Project.objects.get(pk=task.project.pk)
#         user_pk_list = Team.objects.filter(project=project, end=None).distinct().values_list('user_id', flat=True)
#         if self.request.user.pk in user_pk_list:
#             return True
#         else:
#             return False


# class TaskDeleteView(PermissionRequiredMixin, UserPassesTestMixin, SessionStatMixin, DeleteView):
#     model = Task
#     context_object_name = 'task'
#     template_name = 'task/delete.html'
#     success_url = reverse_lazy('webapp:index')
#     permission_required = 'webapp.delete_task'
#     permission_denied_message = 'Access is denied!'


#     def test_func(self, **kwargs):
#         task = Task.objects.get(pk=self.kwargs.get('pk'))
#         project = Project.objects.get(pk=task.project.pk)
#         team = Team.objects.filter(project=project, end=None).distinct()
#         user_pk_list = team.values_list('user_id', flat=True)
#         if self.request.user.pk in user_pk_list:
#             return True
#         else:
#             return False

