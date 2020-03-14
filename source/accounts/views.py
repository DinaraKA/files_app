from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import DetailView
from django.contrib.auth.models import User
from accounts.forms import UserCreationForm
from accounts.models import Profile


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
            Profile.objects.create(user=user, avatar=form.cleaned_data['avatar'])
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_object'





