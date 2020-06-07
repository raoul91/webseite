from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Poll, Choice
from django.urls import reverse


def index(request):
    value = "0"
    whatever = "1"

    if(request.POST.get('mybtn')):
        #value = request.GET.get('mytextbox')
        value = request.POST.get('mybtn') + "B"

    context = {'Umfragen' : Poll.objects.all(), 'Titel': "Umfrageseite", "Value": value, "whatever" : whatever}
    return render(request=request, template_name = 'polls/index.html', context=context)


def umfrage_detail(request, slug):
    #umfrage = Poll.objects.get(slug = slug)
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage' : umfrage}
    return render(request=request, template_name = 'polls/umfrage.html', context=context)

def vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        ausgewaehlte_antwort = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse('Fehler: es wurde eine ungueltige antwort gewaehlt..')
    else:
        ausgewaehlte_antwort.votes += 1
        ausgewaehlte_antwort.save()
        return HttpResponseRedirect(reverse('results', args=(umfrage.slug, )))

def results(request, slug):
    #umfrage = Poll.objects.get(slug = slug)
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage' : umfrage}
    return render(request=request, template_name = 'polls/results.html', context=context)



def myFunction(request):
    if request.method == 'POST':
        input = request.POST.get('textfield', None)
        context = {'antwort' : 'nothing found'}
    else:
        context = {'antwort' : 'nothing found'}

    return render(request, template_name = 'polls/antwort.html')
