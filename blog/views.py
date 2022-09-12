from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentBox


@login_required
def view_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts.html', context)


@login_required
def view_post_info(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.order_by('-created_on')
    comment = None
    if request.method == "POST":
        comment_box = CommentBox(request.POST)
        if comment_box.is_valid():
            comment_box.instance.name = request.user.username
            comment = comment_box.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been added')
            return redirect('view_post_info', slug=slug)
    else:
        comment_box = CommentBox()
    
    context = {
        'comments': comments,
        'comment_box': comment_box,
        'post': post
    }
    return render(request, 'post_info.html', context)