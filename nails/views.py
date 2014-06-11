from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.core.mail import send_mail

class contactform(forms.Form):
	sender=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'type':'text','name':'user','class':'input'}))
	phone=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'type':'text','name':'sdfg','class':'input'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'type':'text','name':'payuity','class':'input'}))
	message=forms.CharField(min_length=5,widget=forms.TextInput(attrs={'type':'text','name':'user','class':'textarea'}))



def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def product(request):
	return render(request,'product.html')

def contact(request):
	if request.method == 'POST':
		form=contactform(request.POST)
		if form.is_valid():
			sender= form.cleaned_data['sender']
			phone= form.cleaned_data['phone']
			email= form.cleaned_data['email']
			message= form.cleaned_data['message']
			send_mail(phone,message,sender+'<'+email+'>',('newbrightnails@gmail.com',), fail_silently=True)

			return HttpResponseRedirect('/contact/')
	else:
		form=contactform()		

	return render(request,'contact.html',{'form':form,}) 