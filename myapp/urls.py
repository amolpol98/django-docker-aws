"""URLs for the ``myapp`` app."""
from django.conf.urls import url

from django.views.generic import TemplateView

urlpatterns = [
    url('', TemplateView.as_view(template_name='home2.html')),
]
