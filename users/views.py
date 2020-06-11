from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from quiz.models import Quiz
from django.views.generic import DetailView
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your Account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def myprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been updated!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    my_quizes = Quiz.objects.filter(author=request.user)
    context = {
        'title': 'Profile',
        'u_form': u_form,
        'p_form': p_form,
        'quizes': my_quizes,
    }
    return render(request, 'users/profile.html', context)


class UserProfiles(DetailView):
    model = User
    template_name = 'users/userprofiles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context_entry = "Profile"
        my_quizes = Quiz.objects.filter(author=self.object)
        context["title"] = new_context_entry
        context["quizes"] = my_quizes
        return context