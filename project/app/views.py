from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, ImageForm

from .models import Post, Category, Comments, Likes


class GetPosts(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'


class GetDetail(DetailView):
    model = Post


class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/proj'


class UpdatePost(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/proj'


class DeletePost(DeleteView):
    model = Post
    success_url = '/proj'


def index(request):
    posts = Post.objects.all().select_related('likes').prefetch_related('category')
    likes = Post.objects.all()
    com = Post.objects.all()
    cats = Post.objects.all()
    return render(request, 'app/test.html',
                  context={'posts': posts, 'Likes': likes, 'coms': com, 'cats': cats})


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
        else:
            form = ImageForm()
        return render(request, 'index.html', {'form': form})
