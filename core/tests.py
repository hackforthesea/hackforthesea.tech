from django.test import TestCase

from mysite.core import views as core_views

urlpatterns = [
    ...
    url(r'^signup/$', core_views.signup, name='signup'),
]