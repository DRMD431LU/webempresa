from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Inicio")
	 
def about(request):
	return HttpResponse("Acerca")
	
def services(request):
	return HttpResponse("Servicois")
	
def store(request):
	return HttpResponse("store")
	
def contact(request):
	return HttpResponse("contact")
	
def blog(request):
	return HttpResponse("blog")
	
def sample(request):
	return HttpResponse("sample")