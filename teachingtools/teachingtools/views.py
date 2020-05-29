from django.shortcuts import render
from django.http import HttpResponse

from .models import Tool, Category

# Create your views here.
def index(request):
    all_tools = Tool.objects.order_by('id')
    all_categories = Category.objects.order_by('id')
    context = {'tool_list': all_tools, 'categories': all_categories}

    return render(request, 'filtertools/index.html', context)