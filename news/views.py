from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from .models import Story


def index(request):
    latest_story_list = Story.objects.order_by('-pub_date')[:5]
    context = {'latest_story_list': latest_story_list}
    return render(request, 'news/index.html', context)


    
def detail(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'news/detail.html', {'story':story})