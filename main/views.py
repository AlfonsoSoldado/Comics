from django.shortcuts import render_to_response, get_object_or_404, render, \
    get_list_or_404
from django.template import RequestContext

from main.forms import ComicForm
from main.models import Comic
from main.populate import populateDatabase


Prefs={}   # matriz de usuarios y puntuaciones a cada a items
ItemsPrefs={}   # matriz de items y puntuaciones de cada usuario. Inversa de Prefs
SimItems=[]  # matriz de similitudes entre los items

# Funcion que carga en el diccionario Prefs todas las puntuaciones de usuarios a peliculas. Tambien carga el diccionario inverso y la matriz de similitud entre items
# Serializa los resultados en dataRS.dat

#  CONJUNTO DE VISTAS

def index(request): 
    return render_to_response('index.html')

def populateDB(request):
    populateDatabase() 
    return render_to_response('populate.html')

def search(request):
    if request.method=='GET':
        form = ComicForm(request.GET, request.FILES)
        if form.is_valid():
            idComic = form.cleaned_data['comicTitle']
            comic = get_list_or_404(Comic, comicTitle__contains=idComic)
            return render_to_response('comics.html', {'comic': comic})
    else:
        form=ComicForm()
    return render_to_response('search_comic.html', {'form':form }, context_instance=RequestContext(request))
