from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
   Data = {'Posts': Post.objects.all().order_by('-date')}
   return render(request, 'blog.html', Data)

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})

