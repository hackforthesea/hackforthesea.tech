from django.conf import settings

def site(request):
    return {'SITE_URL': settings.SITE_URL}

def jupyterhub_port(request):
    return {'JUPYTERHUB_PORT': settings.JUPYTERHUB_PORT}