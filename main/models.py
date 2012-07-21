from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length = 255, unique = True)

    def __unicode__(self):
        return self.name

admin.site.register(Group)

class Proposal(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = (("group", "name"),)

    def __unicode__(self):
        return u"%s > %s"%(self.group, self.name)

class ProposalAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']

admin.site.register(Proposal, ProposalAdmin)


class UserProposal(models.Model):
    user = models.ForeignKey(User)
    proposal = models.ForeignKey(Proposal, related_name="userproposal")

    class Meta:
        unique_together = (("user", "proposal"),)

    def __unicode__(self):
        return self.proposal.__unicode__()

admin.site.register(UserProposal)


class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    proposals = models.ManyToManyField(UserProposal, related_name="usergroup")

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ['user', 'group']

admin.site.register(UserGroup, UserGroupAdmin)