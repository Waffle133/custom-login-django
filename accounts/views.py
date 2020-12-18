from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth import logout as django_logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class SignupView(FormView):
    """sign up user view"""
    form_class = forms.SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        """ process user signup"""
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        return super(SignupView, self).get(request)


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required
def test(request):
    if request.user.has_perm('can_publish'):
        return redirect('/')
    return redirect('/')


def logout(request):
    """logout logged in user"""
    django_logout(request)
    return redirect('login')


def create_permission(request):
    content_type = ContentType.objects.get_for_model(get_user_model())
    permission = Permission.objects.get(content_type=content_type, codename='can_publish')
    if permission is None:
        permission = Permission.objects.create(
            codename='can_publish',
            name='Can Publish Posts',
            content_type=content_type,
        )
    request.user.user_permissions.add(permission)

    return redirect('/')


def remove_permission(request):
    content_type = ContentType.objects.get_for_model(get_user_model())
    permission = Permission.objects.get(content_type=content_type, codename='can_publish')
    request.user.user_permissions.remove(permission)
    return redirect('/')


class LoginView(FormView):
    """login view"""

    form_class = forms.LoginForm
    success_url = reverse_lazy('dashboard')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data
        user = authenticate(username=credentials['username'],
                            password=credentials['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('login'))

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        return super(LoginView, self).get(request)
