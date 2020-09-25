from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Riwayat
from .forms import RiwayatForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CreateRiwayat(LoginRequiredMixin, CreateView):
    form_class = RiwayatForm
    template_name = 'riwayat/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ListRiwayat(LoginRequiredMixin, ListView):
    model = Riwayat
    paginate_by = 3
    ordering = ['-time']
    template_name = 'riwayat/list.html'

def get_queryset(self):
    self.queryset = self.model.objects.filter(user=self.request.user)
    return super().get_queryset()

class UpdateRiwayat(LoginRequiredMixin, UpdateView):
    form_class = RiwayatForm
    model = Riwayat
    template_name = 'riwayat/create.html'
