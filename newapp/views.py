from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.
def movie_list(request):
    movie_objects = Movies.objects.all()
    #for search bar
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        # name__icontains job is to display contents which are similar to the text entered in search bar
        movie_objects = movie_objects.filter(name__icontains=movie_name)
    #paginator for page wgich uses 4 movies per page
    paginator = Paginator(movie_objects,3)
    #this will get the current page number
    page = request.GET.get('page')
    #this will fetch the current page objects
    movie_objects = paginator.get_page(page)
    return render(request,'newapp/movies_list.html',{'movie_objects':movie_objects})
