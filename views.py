from django.shortcuts import render
# Create your views here.
from .models import defi, bookMark
from .forms import bookMarkForm

def index(request):
   dd = defi.objects.all()
   book = bookMark.objects.all()
   form = bookMarkForm()

   if request.method == 'POST':
        form = bookMarkForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bff/index.html', {"dd":dd , "book":book , "form":form} )
        else:
            return render(request, 'bff/error.html', {'form':form})
   else:

        return render(request,'bff/index.html',{"dd":dd , "book":book , "form":form})

   return render(request, 'bff/index.html', {"dd":dd , "book":book , "form":form} )
