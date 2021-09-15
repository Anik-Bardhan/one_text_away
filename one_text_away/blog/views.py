from django.shortcuts import render,redirect
from blog.models import Posts
from blog.forms import CommentForm,PostForm
# Create your views here.
def index(requests):
    post=Posts.objects.all()
    return render(requests,'blog/frontpage.html',{'posts':post})

def post_detail(requests,slug):
    post=Posts.objects.get(slug=slug)
    if requests.method=='POST':
        form=CommentForm(requests.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()

            return redirect('post_detail',slug=post.slug)
    else:
        form=CommentForm()
    return render(requests, 'blog/post_detail.html', {'post': post,'form': form})

def write(request):
    post=Posts.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #blog=form.save(commit=True)
            #blog.save()
            form.save()

    else:
        form=PostForm()
    return render(request,"blog/blog_write.html",{'post': post,'form': form})