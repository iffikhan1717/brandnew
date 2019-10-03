from django.shortcuts import render, get_object_or_404
from .models import Post
def homeview(request):
    return render(request,'startpage.html')

def tajikabad(reqest):
    return render(reqest, 'tajikabad/project_details_page.html')

def jinnah(reqest):
    return render(reqest, 'jinnah/project_details.html')


def ms(reqest):
    return render(reqest, 'ms/project_detail.html')

def ms_heights(reqest):
    return render(reqest, 'ms_heights_aprt/project_detail.html')


def latest_project(request):
    return  render(request,'lastest.html')


def aboutus(request):
    return render(request,'about.html')

def contact_us(request):
    return  render(request,'contact us.html')


def posts(request):
    allps = Post.objects.all()
    return render(request,'blog/post-lists.html',{'allps':allps})

def sig_post(request, pos_id):
    a = get_object_or_404(Post, pk=pos_id)
    context = {'ss':a}
    return render(request, 'blog/post.html',context)