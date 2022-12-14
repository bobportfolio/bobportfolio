import django
from django.shortcuts import render
from platform import python_version
from bootstrap5.bootstrap import get_bootstrap_setting
from portfolio.models import Projects, Urls


def find_bootstrap_version_from_href():
    css_url = get_bootstrap_setting("css_url")
    if isinstance(css_url, dict):
        href = css_url.get("href")
        if href:
            words = href.split("bootstrap@")
            if len(words) > 1:
                vers = words[1].split('/')
                return vers[0]
    return 5


def get_versions():
    args = {}
    v = django.VERSION
    args['django_version'] = "%d.%d.%d" % (v[0], v[1], v[2])
    args['python_version'] = python_version()
    args['bootstrap_version'] = find_bootstrap_version_from_href()
    return args


def index(request):
    return render(request, 'portfolio/index.html', get_versions())


def projects(request):
    args = {}
    args['projects'] = Projects.objects.all()
    args['urls'] = Urls.objects.all()
    args.update(get_versions())
    return render(request, 'portfolio/projects.html', args)
