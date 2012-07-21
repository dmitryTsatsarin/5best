from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.aggregates import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from main.models import UserGroup, Group, Proposal, UserProposal
from django.contrib import auth

def index(request):
    groups = []
    for group in Group.objects.filter():
        group.proposals = UserProposal.objects.filter(proposal__group = group).annotate(dcount=Count("usergroup")).order_by("-dcount")
        if len(group.proposals) > 0:
            groups.append(group)

    data = {
        'groups':groups,
    }
    return render_to_response('index.html', data,
                                          context_instance=RequestContext(request))


def dashboard(request):
    return HttpResponseRedirect(reverse("profile", args=[request.user.id]))


def profile(request, id):
    user = get_object_or_404(User, id = id)
    groups = UserGroup.objects.filter(user = user)
    #for groupobj in groups:
    #    groupobj.proposals = UserProposal.objects.filter(proposal__group = groupobj).annotate(dcount=Count("usergroup")).order_by("-dcount")

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


def groups(request):
    #groups = Group.objects.filter()
    return render_to_response('groups.html')