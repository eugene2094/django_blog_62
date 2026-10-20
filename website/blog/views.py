from django.shortcuts import render
from django.utils import timezone
def dummy():
    return "func working!"

# Create your views here.
def index(request):

    context = {"title":"Blog",'text':'Hello World',
               'colors':('red','green','blue'),
               'func':dummy,
               'today':timezone.now(),
               }
    return render(request, 'blog/index.html', context)
