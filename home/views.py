from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # print()
            return HttpResponse('done!')
        else:
            return HttpResponse('not valid')
    
    form = ContactForm()
    return render(request,'contact_page.html',{'form':form} )