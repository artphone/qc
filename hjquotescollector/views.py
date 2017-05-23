from django.shortcuts import render
from django.http import HttpResponseRedirect
from hjquotescollector.models import HjQuote
from hjquotescollector.forms import HjQuoteForm
# Create your views here.

def index(request):
        if (request.method == "POST"):
                        f = HjQuoteForm(request.POST)
                        if f.is_valid():
                                        a = Quote
                                        n_quote_text = f.cleaned_data['quote_form_text']
                                        n_owner = f.cleaned_data['quote_form_owner']
                                        Quote(quote_text = n_quote_text, quote_owner = n_owner).save()
                                        return HttpResponseRedirect('results/')
        else:
                form = HjQuoteForm()

        return render(request, 'index.html', {'form':form} )

def results(request):
        object_list = HjQuote.objects.all()
        context = {'object_list':object_list}
        return render(request, 'results.html', context)
