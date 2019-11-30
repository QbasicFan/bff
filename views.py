from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout

from django.contrib.auth.models import User

from django.db.models import Q


# Create your views here.
from .models import defi, bookMark, defiCard
from .forms import  defiForm, RegistrationForm, UserForm, defiCardForm




def userView(request):

    if request.user.is_authenticated():

        todo = request.user
        defini = defiCard.objects.all()

        return render(request, 'home/userProfile.html', {"todo":todo, "defini":defini} )

    else:
        index(request)



def addWord(request):

    if request.user.is_authenticated():
        if request.method == 'POST':

            form = defiCardForm(request.POST or None,  request.user)

            if form.is_valid():


                cas = defiCard.objects.create(
                author = request.user,
                title = form.cleaned_data['title'],
                mr = form.cleaned_data['mr'],
                fr = form.cleaned_data['fr'],
                en = form.cleaned_data['en'],
                sp = form.cleaned_data['sp'],
                hasAudio = False,

                )
                cas.save()

                return render(request, 'home/error.html', {"form":"Definition has been succellfully added "})
            else:
                return render(request, 'home/error.html', {"form":form})
        else:
            form = defiCardForm()
            return render(request,'home/addWord.html',{'form':form})
    else:
            return render(request, 'home/error.html', {"form":"user is not auth!!!"})




def userProfile(request):
   users = User.objects.all()
   return render(request, 'home/user.html', {"users":users} )

def FavLike(request):
   dd = defi.objects.order_by('?')[:2]

   return render(request, 'home/like.html', {"dd":dd} )

def index(request):
   dd = defi.objects.order_by('?')[:2]
   book = bookMark.objects.all()
   form = defiForm()

   if request.method == 'POST':
        form = defiForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data['title']
            dd = defi.objects.filter(Q(title=f) | Q(mr=f) | Q(fr=f) | Q(en=f) | Q(sp=f) )
            return render(request, 'home/index.html', {"dd":dd , "book":book , "form":form} )
        else:
            return render(request, 'home/error.html', {'form':form})
   else:

        return render(request,'home/index.html',{"dd":dd , "book":book , "form":form})

   return render(request, 'home/index.html', {"dd":dd , "book":book , "form":form} )






#register a new user

def createUser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user.set_password(password1)
            user.save()
            user = authenticate(username=username , password = password1)



            if user is not None:
             if user.is_active:
                login (request , user)
                return render(request, 'home/registerOk.html', {})

            #return render(request, 'register/registerOk.html', {})
        else:
            return render(request, 'home/error.html', {'form':form})
    else:
        form = RegistrationForm()

        return render(request,'home/register.html',{'form':form })

def loggedout(request):
    logout(request)
    return render(request, 'home/error.html', {"form":"You have logged out"})


def logging(request):
      username = request.POST.get('username','')
      password = request.POST.get('password','')
      user = authenticate(username=username , password = password)
      if user is not None:
          if user.is_active:
            login (request , user)
            index(request)

          else:
            return render(request, 'home/error.html', {})
      return render(request, 'home/login.html', {"form":UserForm})








### must go

