from django.shortcuts import render
from django.http import HttpResponseRedirect
from quotescollector.models import Quote
from quotescollector.forms import QuoteForm
# Create your views here.

def index(request):
	if (request.method == "POST"):
			f = QuoteForm(request.POST)
			if f.is_valid():
					a = Quote
					n_quote_text = f.cleaned_data['quote_form_text']
					n_owner = f.cleaned_data['quote_form_owner']
					Quote(quote_text = n_quote_text, quote_owner = n_owner).save()
					return HttpResponseRedirect('results/')
	else:
		form = QuoteForm()

	return render(request, 'index.html', {'form':form} )

def results(request):
	object_list = Quote.objects.all()
	context = {'object_list':object_list}
	return render(request, 'results.html', context)