from django.shortcuts import render,redirect
from django.http import HttpResponse

from . import myquerry

# Create your views here.
def landingPage(request):
	return render(request,"index.html")
def home(request):
	return HttpResponse("Hi")

def calculator(request):
	a=request.POST.get('1st')
	b=request.POST.get('2nd')

	d={}
	if a!=None and b!=None:
		s= int(a)+int(b)
		d={'ad':s}

	

	return render(request,'calci.html',d)
def userdata(request):
	a=request.POST.get('nm')
	b=request.POST.get('em')
	c=request.POST.get('ph')
	
	if a!=None and b!=None and c!=None:
		print(a,b,c)
		myquerry.insertuserdata(a,b,c)
		return render(request,'userform.html',{'stat':"Data inserted"})
	else:
		return render(request,'userform.html',{'stat':"Data not inserted"})

def fetchdata_user_all(request):
	data=myquerry.fetchuserdata()
	print(data)
	return render(request,'table_details.html',{'details':data})

def update_userdata(request):
	id=request.GET.get('v')
	data=myquerry.fetchuser_details(id)
	print(data[0][1])
	user_data={

		'name' : data[0][1],
		'mail' : data[0][2],
		'phone' : data[0][3]

	}
	a=request.POST.get('nm')
	b=request.POST.get('em')
	c=request.POST.get('ph')
	
	if a!=None and b!=None and c!=None:
		print(a,b,c)
		myquerry.updateuserdata(a,b,c,id)
		return redirect('fetchdata')
	return render(request,'update.html',{'data' : user_data})

def deleteuserdata(request):
	id=request.GET.get('v')

	myquerry.deluserdata(id)
	return redirect('fetchdata')