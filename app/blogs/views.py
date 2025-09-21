from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Blog, Comment
from .forms import BlogForm, CommentForm

# ----------------------
# Public Views
# ----------------------

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

# ----------------------
# Login required + Role-based Views
# ----------------------

@login_required
def blog_create(request):
    if not (request.user.is_teacher or request.user.is_admin):
        return HttpResponseForbidden("You are not allowed to create a blog.")

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blogs:blog_detail', blog_id=blog.id)
    else:
        form = BlogForm()
    return render(request, 'blogs/blog_create.html', {'form': form})

@login_required
def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if not (request.user == blog.author or request.user.is_admin):
        return HttpResponseForbidden("You are not allowed to edit this blog.")

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/blog_edit.html', {'form': form, 'blog': blog})

@login_required
def blog_comments(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('blogs:blog_comments', blog_id=blog.id)
    else:
        form = CommentForm()
    return render(request, 'blogs/blog_comments.html', {'blog': blog, 'form': form})
