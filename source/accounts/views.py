from django.views.generic import DetailView
from django.contrib.auth.models import User
from webapp.models import File


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = User.objects.get(pk=self.kwargs['pk'])
        context['self_files'] = File.objects.filter(author=user.pk)
        context['files'] = File.objects.filter(access='base').order_by('-date')
        return context





