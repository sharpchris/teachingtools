from django.urls import path

# Replaces the standard django.conf.path, identical syntax
from django_distill import distill_path

from . import views

def get_index():
    # The index URI path, '', contains no parameters, named or otherwise.
    # You can simply just return nothing here.
    return None

urlpatterns = [
     distill_path('', 
                views.index,
                name='index',
                distill_func=get_index,
                 # / is not a valid file name! override it to index.html
                 distill_file='index.html')
]