from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

from portfolio.forms import BlogPostForm
from portfolio.models import BlogPost


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def sobre_mim_page_view(request):
    return render(request, 'portfolio/sobre.html')


def blog_page_view(request):
    elementos = BlogPost.objects.all()

    return render(request, 'portfolio/blog.html', {"posts": elementos})


def novo_post_view(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/novo_post.html', context)


def editar_post_view(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    form = BlogPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}

    return render(request, 'portfolio/editar_post.html', context)


def apagar_post_view(request, post_id):
    BlogPost.objects.get(pk=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')

def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')

def tfc_page_view(request):
    return render(request, 'portfolio/tfc.html')

def video_page_view(request):
    return render(request, 'portfolio/video.html')