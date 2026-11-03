from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .forms import PostForm
from .models import Post, Category, Tag
from django.db.models import Q


def get_categories():
    categories = Category.objects.all()
    first_half = Category.objects.all()[:len(categories) // 2]
    second_half = Category.objects.all()[len(categories) // 2:]
    return {'categories': first_half, 'categories2': second_half}


# Create your views here.
def index(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()

    category_id = request.GET.get('category', None)
    query = request.GET.get('q', "").strip()

    if category_id:
        posts = posts.filter(category=category_id)

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {'posts': posts, 'tags': tags,'selected_category': category_id}
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


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})


def post_update(request, id):
    post = get_object_or_404(Post, id=id,user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form})


