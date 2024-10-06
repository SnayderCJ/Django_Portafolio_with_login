from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "blog.html", {"posts": posts, "total_posts": total_posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})