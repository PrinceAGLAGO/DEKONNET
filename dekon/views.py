from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Annonce, Exigence
from .forms import AnnonceForm, ExigenceForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'website/base.html')

def electronics(request):
    return render(request, 'website/electronics.html')
def fashion(request):
    return render(request, 'website/fashion.html')
def jewellery(request):     
    return render(request, 'website/jewellery.html')
def alimentation(request):
    return render(request, 'website/alimentation_artisanale.html')
def animaux(request):
    return render(request, 'website/animaux_compagnie.html')
def art(request):
    return render(request, 'website/art_objet_collection.html')
def automobile(request):
    return render(request, 'website/automobile.html')
def beaute(request):
    return render(request, 'website/beaute_soins.html')
def bricolage(request):
    return render(request, 'website/bricolage_amenagement.html')
def enfant(request):
    return render(request, 'website/enfants_bebe.html')
def livre(request):
    return render(request, 'website/livre_media.html')
def service(request): 
    return render(request, 'website/service_cours.html')
def modedurable(request):
    return render(request, 'website/mode_durable_ethique.html')
def sport(request):
    return render(request, 'website/sport_loisirs.html')
def voyage(request): 
    return render(request, 'website/voyage_echanges.html')
def sante(request): 
    return render(request, 'website/sante.html')
def decoration(request): 
    return render(request, 'website/decoration.html')
def jardin(request): 
    return render(request, 'website/jardin.html')
def maison(request): 
    return render(request, 'website/maison.html')
def cuisine(request):
    return render(request,'website/ustensils_cuisine.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def index(request):
    return render(request, 'index.html')
def logout_view(request):
    # Logique de déconnexion
    return render(request, 'logout.html')
def widgets(request):
    return render(request, 'pages/widgets.html')
def morris(request):
    return render(request, 'pages/charts/morris.html')
def flot(request):
    return render(request, 'pages/charts/flot.html')
def inline(request):
    return render(request, 'pages/charts/inline.html')
def general(request):
    return render(request, 'pages/UI/general.html')
def icons(request):
    return render(request, 'pages/UI/icons.html')
def buttons(request):
    return render(request, 'pages/UI/buttons.html')
def sliders(request):
    return render(request, 'pages/UI/sliders.html')
def timeline(request):
    return render(request, 'pages/UI/timeline.html')
def general_elements(request):
    return render(request, 'pages/forms/general.html')
def advanced_elements(request):
    return render(request, 'pages/forms/advanced.html')
def editors(request):
    return render(request, 'pages/forms/editors.html')
def simple_tables(request):
    return render(request, 'pages/tables/simple.html')
def data_tables(request):
    return render(request, 'pages/tables/data.html')
def calendar(request):
    return render(request, 'pages/calendar.html')
def mailbox(request):
    return render(request, 'pages/mailbox.html')
def invoice(request):
    return render(request, 'pages/examples/invoice.html')
def login(request):
    return render(request, 'pages/examples/login.html')
def register(request):
    return render(request, 'pages/examples/register.html')
def lockscreen(request):
    return render(request, 'pages/examples/lockscreen.html')
def error_404(request):
    return render(request, 'pages/examples/404.html')
def error_500(request):
    return render(request, 'pages/examples/500.html')
def blank_page(request):
    return render(request, 'pages/examples/blank.html')

# @login_required
def soumettre_annonce(request):
    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES)
        if form.is_valid():
            annonce = form.save(commit=False)
            annonce.user = request.user
            annonce.save()
            return redirect('home')
    else:
        form = AnnonceForm()
    return render(request, 'dekon/soumettre_annonce.html', {'form': form})

def detail_annonce(request, annonce_id):
    annonce = Annonce.objects.get(id=annonce_id)
    return render(request, 'dekon/detail_annonce.html', {'annonce': annonce})

# # @login_required
# def creer_annonce(request):
#     if request.method == 'POST':
#         form = AnnonceForm(request.POST, request.FILES)
#         if form.is_valid():
#             annonce = form.save(commit=False)
#             annonce.user = request.user
#             annonce.save()
#             return redirect('ajouter_exigences', annonce_id=annonce.id)
#     else:
#         form = AnnonceForm()
#     return render(request, 'dekon/annonce/creer.html', {'form': form})

@login_required
def ajouter_exigences(request, annonce_id):
    annonce = Annonce.objects.get(id=annonce_id, user=request.user)
    if request.method == 'POST':
        form = ExigenceForm(request.POST)
        if form.is_valid():
            exigence = form.save(commit=False)
            exigence.annonce = annonce
            exigence.save()
            return redirect('dashboard')
    else:
        form = ExigenceForm()
    return render(request, 'dekon/annonce/exigences.html', {'form': form, 'annonce': annonce})

def liste_annonces(request):
    annonces = Annonce.objects.filter(statut='actif')
    return render(request, 'dekon/liste_annonces.html', {'annonces': annonces})


def dashboard_abonnee(request):
    if request.user.is_authenticated:
        annonces = Annonce.objects.filter(user=request.user)
        return render(request, 'dekon/dashboard_abonnee.html', {'annonces': annonces})
    else:
        return redirect('login')