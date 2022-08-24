import django
from django.shortcuts import render
from platform import python_version
from bootstrap5.bootstrap import get_bootstrap_setting


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


def index(request):
    args = {}
    v = django.VERSION
    args['django_version'] = "%d.%d.%d" % (v[0], v[1], v[2])
    args['python_version'] = python_version()
    args['bootstrap_version'] = find_bootstrap_version_from_href()
    return render(request, 'portfolio/index.html', args)
