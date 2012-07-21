from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length = 255, unique = True)

admin.site.register(Group)

class Proposal(models.Model):
    name = models.CharField(max_length=255, unique = True)

admin.site.register(Proposal)

class UserProposal(models.Model):
    proposal = models.ForeignKey(Proposal)
    placenumber = models.PositiveIntegerField()

admin.site.register(UserProposal)

class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    proposals = models.ManyToManyField(UserProposal)

admin.site.register(UserGroup)