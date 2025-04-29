from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from forms import *


# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)
            return redirect('home')
    else:
        form = InscriptionForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(data=request.POST)
        if form.is_valid():
            utilisateur = form.get_user()
            login(request, utilisateur)
            return redirect('home')
    else:
        form = ConnexionForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('connexion')
