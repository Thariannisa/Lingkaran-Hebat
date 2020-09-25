from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Inspiration, Like, Clap
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ListInspiration(LoginRequiredMixin, ListView):
    template_name = "inspiration/list.html"
    ordering = ['-time']
    model = Inspiration
    paginate_by = 2

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        try:
            if request.FILES['image']:
                myfile = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save("inspirasi/"+myfile.name, myfile)
                inspirasi = Inspiration.objects.create(
                    title=title, image=filename, user=request.user, countLike=0, countClap=0)
        except KeyError:
            inspirasi = Inspiration.objects.create(
                title=title, user=request.user, countLike=0, countClap=0)
        inspirasi.save()
        return redirect('inspiration:list')

    def get_queryset(self):
        try:
            print(self.request.GET.get('search'))
            self.queryset = self.model.objects.filter(
                title__icontains=self.request.GET['search'])
        except KeyError:
            pass
        return super().get_queryset()


class DetailInspiration(LoginRequiredMixin, DetailView):
    template_name = "inspiration/detail.html"
    model = Inspiration


def Likes(request, *args, **kwargs):
    tinspirasi = Inspiration.objects.get(id=kwargs['pk'])
    if Like.objects.filter(user=request.user, inspiration=kwargs['pk']).count() != 1:
        like = Like(user=request.user, inspiration=tinspirasi)
        like.save()
        Inspiration.objects.filter(id=kwargs['pk']).update(
            countLike=(tinspirasi.countLike+1))
    return redirect("inspiration:list")


def Claps(request, *args, **kwargs):
    tinspirasi = Inspiration.objects.get(id=kwargs['pk'])
    if Clap.objects.filter(user=request.user, inspiration=kwargs['pk']).count() != 1:
        clap = Clap(user=request.user, inspiration=tinspirasi)
        clap.save()
        Inspiration.objects.filter(id=kwargs['pk']).update(
            countClap=(tinspirasi.countClap+1))
    return redirect("inspiration:list")
