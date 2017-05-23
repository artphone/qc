from django import forms



class HjQuoteForm(forms.Form):
        quote_form_text = forms.CharField(label = 'Give me Quotes', max_length=1000)
        quote_form_owner = forms.CharField(label = 'owner', max_length=100)