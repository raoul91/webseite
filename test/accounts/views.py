from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import HomeForm
from .logic import outputText

# Create your views here.
"""
def home(request):
    return render(request, 'accounts/login.html')
"""

class HomeView(TemplateView):
    template_name = 'accounts/index.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            result = outputText(text)
            args = { 'form':form, 'result' : result }
            return render(request, self.template_name, args)


def forCyrill(request):
    return render(request, 'accounts/forCyrill.html')


def forSilvan(request):
    return render(request, 'accounts/forSilvan.html')
