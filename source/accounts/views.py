from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import DetailView
from django.contrib.auth.models import User
from accounts.forms import UserCreationForm
from accounts.models import Profile
from webapp.models import File


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = User.objects.get(pk=self.kwargs['pk'])
        context['files'] = File.objects.filter(author=user.pk)
        return context





