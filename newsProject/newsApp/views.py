from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "index.html", {
        'posts': posts
    })

#upd
def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post-detail.html", {
        'post': post
    })