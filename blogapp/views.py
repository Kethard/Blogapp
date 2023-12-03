from django.shortcuts import render

from blogapp.models import Post


def post_page(request, slug):
    post= Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'blogapp/post.html',context)
