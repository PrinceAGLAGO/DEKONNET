from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('electronics/', views.electronics, name='electronics'),
    path('fashion/', views.fashion, name='fashion'),
    path('jewellery/', views.jewellery, name='jewellery'),
    path('alimentation/', views.alimentation, name='alimentation'),
    path('animaux/', views.animaux, name='animaux'),
    path('art/', views.art, name='art'),
    path('automobile/', views.automobile, name='automobile'),
    path('beaute/', views.beaute, name='beaute'),
    path('bricolage/', views.bricolage, name='bricolage'),
    path('enfant/', views.enfant, name='enfant'),
    path('livre/', views.livre, name='livre'),
    path('service/', views.service, name='service'),
    path('modedurable/', views.modedurable, name='modedurable'),
    path('sport/', views.sport, name='sport'),
    path('voyage/', views.voyage, name='voyage'),
    path('maison/', views.maison, name='maison'),
    path('decoration/', views.decoration, name='decoration'),
    path('cuisine/', views.cuisine, name='cuisine'),
    path('jardin/', views.jardin, name='jardin'),
    #path('musique/', views.musique, name='musique'),
    path('sante_sexuel/', views.sante, name='sante'),
    path('cuisine/', views.cuisine, name='cuisine'),
    path('', views.index, name='index'),  # Vue pour index
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),  # Vue pour logout
    path('widgets/', views.widgets, name='widgets'),
    path('morris/', views.morris, name='morris'),
    path('flot/', views.flot, name='flot'),
    path('inline/', views.inline, name='inline'),
    path('UI/general/', views.general, name='general'),
    path('UI/icons/', views.icons, name='icons'),
    path('UI/buttons/', views.buttons, name='buttons'),
    path('UI/sliders/', views.sliders, name='sliders'),
    path('UI/timeline/', views.timeline, name='timeline'),
    path('forms/general/', views.general_elements, name='general_elements'),
    path('forms/advanced/', views.advanced_elements, name='advanced_elements'),
    path('forms/editors/', views.editors, name='editors'),
    path('tables/simple/', views.simple_tables, name='simple_tables'),
    path('tables/data/', views.data_tables, name='data_tables'),
    path('calendar/', views.calendar, name='calendar'),
    path('mailbox/', views.mailbox, name='mailbox'),
    path('examples/invoice/', views.invoice, name='invoice'),
    path('examples/login/', views.login, name='login'),
    path('examples/register/', views.register, name='register'),
    path('examples/lockscreen/', views.lockscreen, name='lockscreen'),
    path('examples/404/', views.error_404, name='error_404'),
    path('examples/500/', views.error_500, name='error_500'),
    path('examples/blank/', views.blank_page, name='blank_page'),
    #path('annonces/creer/', views.creer_annonce, name='creer_annonce'),
    # path('annonces/exigences', views.ajouter_exigences, name='ajouter_exigences'),
    path('liste_annonces/',views.liste_annonces, name='liste_annonces'),
    path('soumettre-annonce/', views.soumettre_annonce, name='soumettre_annonce'),
    path('annonce/<int:annonce_id>/', views.detail_annonce, name='detail_annonce'),
<<<<<<< HEAD


=======
>>>>>>> 12de449c3b4e51304461edeedc09e4c38ce1e550
]