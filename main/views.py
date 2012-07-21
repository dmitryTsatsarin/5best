from django.shortcuts import render_to_response
from django.template.context import RequestContext
from main.models import UserGroup

def index(request):
    groups = UserGroup.objects.filter()
    data = {
        'groups':groups,
    }
    return render_to_response('index.html', data,
                                          context_instance=RequestContext(request))


def dashboard(request):
    return render_to_response('dashboard.html')


def profile(request, id):
    return render_to_response('profile.html')


def group(request, id):
    return render_to_response('group.html')