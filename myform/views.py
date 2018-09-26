from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from myform.models import Contact
from django import forms
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')
        widgets = {
            'message': forms.Textarea(attrs={'cols':20, 'rows': 10,
                'placeholder': 'Entrer votre message ici'}),
            'name': forms.TextInput(attrs={'placeholder': 'Doe'})
        }
        labels = {
        "name": "Nom",
        "firstname": "Prénom",
    }
    


from django import forms

class ContactForm2(forms.Form):
    name = forms.CharField(max_length=50, initial="Votre nom", label="nom")
    firstname = forms.CharField(max_length=50,  initial="Votre prénom", 
    label="prenom")
    email = forms.EmailField(max_length=200, label='mail')
    message = forms.CharField(max_length=1000, 
    widget=forms.Textarea(attrs={'cols':20, 'rows': 10}))


""" def contact(request):
    contact_form = ContactForm()
    contact_form2 = ContactForm2()
    return render(request, 'contact.html', 
    {'contact_form': contact_form,
    'contact_form2': contact_form2  })
 """

def contact(request):
    # on instancie un formulaire
    form = ContactForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ContactForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_contact = form.save()
            return redirect(reverse('detail', args=[new_contact.pk] ))
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request,'contact.html', context)

def edit(request, pers_id):
    # on récupère la personne
    pers = Contact.objects.get(pk=pers_id)
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ContactForm(request.POST, instance=pers)
        # on vérifie la validité du formulaire
        if form.is_valid():
            form.save()
            return redirect(reverse('detail', args=[pers_id] ))
    # Si méthode GET, on présente le formulaire
    form = ContactForm(instance=pers)
    context = {'form': form}
    return render(request,'contact.html', context)

def delete(request, pers_id):
    pers = Contact.objects.get(pk=pers_id)
    pers.delete()
    return render(request,'contact.html')

def detail(request, cid):
    contact = Contact.objects.get(pk=cid)
    return HttpResponse('Nouveau contact '+contact.name+' '+contact.email)


def liste(request):
    objects = Contact.objects.all().order_by('name')
    return render(request, template_name='contact_list.html', context={'objects': objects} )