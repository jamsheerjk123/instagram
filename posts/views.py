from django.shortcuts import render
from .models import POSTS
from .forms import PostAddForm
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'posts/home.html')
    
@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:home')
        else:
            return render(request, 'posts/add_post.html', {'form': form})
    else:
        form = PostAddForm()
        return render(request, 'posts/add_post.html', {'form': form})