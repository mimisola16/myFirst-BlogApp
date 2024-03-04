from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
# def index(request):
#     return HttpResponse("Hello world")

# def myIndex(request):
#     data={
#         'name':'Mariam',
#         'age':20
#     }
#     return render(request, 'index.html', context=data)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    
