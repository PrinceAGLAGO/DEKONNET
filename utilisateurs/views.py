from django.shortcuts import render

# Create your views here.
def inscription(request):
    return render(request, 'utilisateurs/inscription.html')

def connexion(request):
    return render(request, 'utilisateurs/connexion.html')

def deconnexion(request):
    return render(request, 'utilisateurs/deconnexion.html')