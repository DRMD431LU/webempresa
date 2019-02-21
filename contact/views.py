from django.shortcuts import render,HttpResponse,redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse
# Create your views here.

def contact(request):
	print("Tipo: {}".format(request.method))
	contact_form = ContactForm()
	if request.method =="POST":
		contact_form = ContactForm(data=request.POST)
		if contact_form.is_valid():
			name = request.POST.get('name','')
			email = request.POST.get('email','')
			content = request.POST.get('content','')
			#Enviar correo y redireccionar
			email = EmailMessage(
				"La caffettiera: nuevo mensaje",
				"De {} <{}> \n\n Escribió:{}".format(name,email,content),
				"no-contestar@inbox.mailtrap.io",
				["vict.22.r@gmail.com"],
				reply_to=[email]
				)
			try:
				email.send()
				return redirect(reverse('contact')+"?ok")
			except:
				return redirect(reverse('contact')+"?fail")
				
	return render(request,"contact/contact.html",{'form':contact_form})
	
