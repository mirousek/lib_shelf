# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from libs.models import *
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.core.urlresolvers import reverse

def list(request):
    response=''
    
    libraries=Library.objects.all()
    for library in libraries:
        response+=library.name
        response+='<br/>'
        
    t=get_template('library_list.html')
    c=Context({'libraries': libraries})
    response=t.render(c)
    return HttpResponse(response)

def library_add_edit(request, pk=None, slug=None):
    try:
        if pk:
            l = Library.objects.get(pk=pk)
        else:
            l = Library.objects.get(slug=slug)
    except:
        l = None

    if request.method == 'POST':
        f = LibraryForm(request.POST, instance=l)
        if f.is_valid():
            l = f.save()
            return HttpResponseRedirect(reverse('library_detail', args=[l.slug]))
        return render(request, 'libs/library_add.html', {'form': f})
    else:

        f = LibraryForm(instance=l)
        return render(request, 'libs/library_add.html', {'form': f})

#def library_edit(request, slug):
#    return None

#def library_add_edit(request, slug):
    