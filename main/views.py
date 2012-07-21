from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from main.models import UserGroup
from django.contrib import auth

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
    user = get_object_or_404(User, id = id)
    groups = UserGroup.objects.filter(user = user)
    data = {
        'profile' : user,
        'groups' : groups,
    }
    return render_to_response('profile.html', data,
        context_instance=RequestContext(request))


def group(request, id):

    return render_to_response('group.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def login(request):
    return render_to_response('login.html')