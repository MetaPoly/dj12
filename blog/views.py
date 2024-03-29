from django.shortcuts import render
from .models import Blog
# Create your views here.
def allblogs(request):
    blogs=Blog.objects.all
    return render(request,"blog/allblog.html",{"blogs":blogs})

def detail(request, blog_id):
    detailblog=get_object_or_404(Blog,pk=blog_id)
    return render(request,"blog/detail.html",{'blog':detailblog})