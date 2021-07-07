from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group


def index(request):
    latest = Post.objects.order_by('-pub_date')[:10]
    output = []
    for item in latest:
        output.append(item.text)
    return HttpResponse('\n'.join(output))


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})

# Create your views here.