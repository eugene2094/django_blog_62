from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Post, Category, Tag


def get_categories():
    categories = Category.objects.all()
    first_half = Category.objects.all()[:len(categories) // 2]
    second_half = Category.objects.all()[len(categories) // 2:]
    return {'categories': first_half, 'categories2': second_half}


# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {'posts': posts, 'tags': tags}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def get_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {'post': post, 'tags': Tag.objects.all()}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)
