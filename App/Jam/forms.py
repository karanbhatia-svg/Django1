from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class InvestmentForm(forms.Form):
	starting_amount = forms.FloatField()
	number_of_years = forms.FloatField()
	return_rate = forms.FloatField()
	annual_additional_contribution = forms.FloatField()


