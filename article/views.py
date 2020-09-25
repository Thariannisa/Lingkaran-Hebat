from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article, Likes, Claps
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ListArticle(LoginRequiredMixin, ListView):
    template_name = "article/list.html"
    ordering = ['-time']
    model = Article
    paginate_by = 2

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        try:
            if request.FILES['image']:
                myfile = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save("article/"+myfile.name, myfile)
                article = Article.objects.create(
                    title=title, image=filename, user=request.user, countLike=0, countClap=0)
        except KeyError:
            article = Article.objects.create(
                title=title, user=request.user, countLike=0, countClap=0)
        article.save()
        return redirect('article:list')

    def get_queryset(self):
        try:
            print(self.request.GET.get('search'))
            self.queryset = self.model.objects.filter(
                title__icontains=self.request.GET['search'])
        except KeyError:
            pass
        return super().get_queryset()


class DetailArticle(LoginRequiredMixin, DetailView):
    template_name = "article/detail.html"
    model = Article


def Likees(request, *args, **kwargs):
    tarticle = Article.objects.get(id=kwargs['pk'])
    if Likes.objects.filter(user=request.user, article=kwargs['pk']).count() != 1:
        like = Likes(user=request.user, article=tarticle)
        like.save()
        Article.objects.filter(id=kwargs['pk']).update(
            countLike=(tarticle.countLike+1))
    return redirect("article:list")


def Clapes(request, *args, **kwargs):
    tarticle = Article.objects.get(id=kwargs['pk'])
    if Claps.objects.filter(user=request.user, article=kwargs['pk']).count() != 1:
        clap = Claps(user=request.user, article=tarticle)
        clap.save()
        Article.objects.filter(id=kwargs['pk']).update(
            countClap=(tarticle.countClap+1))
    return redirect("article:list")
