from django.http import HttpResponse 
from django.shortcuts import render
import operator

#fonction pour afficher le message 
def helloWorld(request):
    return HttpResponse("<h2>Hello World</h2>")

#fonction pour afficher la page html
def tal(request):
    return render(request,'tal.html')

def recette(request):
    return render(request, 'Recette_tiramisu_boot.html')

def bonjour(request):
    return render(request,'bonjour.html')

def welcome(request):
    prenom_nom = request.GET['prenom_nom'] #on récupère les données grâce à la fonction GET
    print(prenom_nom)
    return render(request, 'affiche.html', {'fullname': prenom_nom})

def compteur(request):
    return render(request,'compteur.html')

def affiche(request):
    compteur_mots = request.GET['texte']
    liste_mots = compteur_mots.split()
    print(compteur_mots)
    word_dict = {}
    for mot in liste_mots:
        if mot in word_dict:
            word_dict[mot]+=1
        else:
            word_dict[mot] = 1 #donner valeur 1 à la clé mot 
    to_sort = sorted(word_dict.items(), key = operator.itemgetter(1), reverse = True)
    return render(request,'afficher.html',{'compteur_mots':compteur_mots, 'liste_mots':len(liste_mots),'to_sort':to_sort})