from django.contrib.auth.models import Group


def create_groups():
    Group.objects.get_or_create(name='Reader')
    Group.objects.get_or_create(name='Journalist')
    Group.objects.get_or_create(name='Editor')
    