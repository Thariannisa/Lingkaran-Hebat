from django.shortcuts import render, redirect
from django.views.generic import FormView, UpdateView
from .forms import UserForm
from django.contrib.auth import authenticate, login
from .models import User
# Create your views here.


class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = UserForm
    success_url = '/inspiration'
    extra_context = {
        'page': 'Lingkaran Hebat - Register',
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        password = form.cleaned_data['password1']
        self.object.set_password(password)
        self.object.save()
        login(self.request, self.object)
        return super().form_valid(form)


class EditView(UpdateView):
    template_name = 'auth/update.html'
    form_class = UserForm
    model = User
    extra_context = {
        'page': 'Lingkaran Hebat - Update Profil',
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        password = form.cleaned_data['password1']
        self.object.set_password(password)
        self.object.save()
        return super().form_valid(form)


def Success(request, *args, **kwargs):
    user = User.objects.get(id=kwargs['pk'])
    login(request, user)
    return redirect("inspiration:list")
