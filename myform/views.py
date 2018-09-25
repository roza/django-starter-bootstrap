from django.shortcuts import render
from django.forms import ModelForm
from myform.models import Contact

# Create your views here.

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')


from django import forms

class ContactForm2(forms.Form):
    name = forms.CharField(max_length=50)
    firstname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(max_length=1000)


def contact(request):
    contact_form = ContactForm()
    contact_form2 = ContactForm2()
    return render(request, 'contact.html', 
    {'contact_form': contact_form,
    'contact_form2': contact_form2  })
