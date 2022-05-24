import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from tutorial_app.users.forms import *
from tutorial_app.users.helper_functions import *
from tutorial_app.users.login import login_func
from tutorial_app.users.show import returnAll
from tutorial_app.users.helper_functions import *


def mainpage(request):
    return HttpResponse("Hello World!")


def printnum(request, num):
    return HttpResponse(f'I print int, it is {num}')


def printstring(request, string):
    return HttpResponse(f'I print string, it is {string}')


def trying(request):
    dat = returnAll()
    return render(request, 'show.html', {"dat":dat})




def loginfirst(request):
    context = {"login_fail": False, "login_form":LoginForm()}
    return render(request, 'tut-app/login.html', context)


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    loginstatus = login_func(username, password)
    if loginstatus == "user":
        request.session['status'] = "user"
        return redirect('../home')
    elif loginstatus == "manager":
        request.session['status'] = "manager"
        return redirect('../home')
    else:
        context = {"login_fail": True, "login_form":LoginForm()}
        return render(request, 'tut-app/login.html', context)


def add_user(request):
    name = request.POST.get("name")
    username = request.POST.get("username")
    institution = request.POST.get("institution")
    password = request.POST.get("password") # hash it
    add_a_user(name, username, institution, password)
    return HttpResponse(f'User Added!')


def drug_page(request):
    return 0
#    drugid = request.POST.get("drugid")
#    info = drug_info(drugid)
#    info["affinity_form"] = DrugIDForm()
#    return render(request, 'drugpage.html', info)


def delete_drug(request):
    drugid = request.POST.get('drugid')
    get_delete_drug(drugid)
    return HttpResponse(f'Drug Deleted!')


def update_affinity(request): # 3
    reactionid = request.POST.get("reactionid")
    affinity = request.POST.get("affinity")
    get_update_affinity(reactionid, affinity)
    return HttpResponse(f'Affinity Updated!')


def delete_protein(request): #4
    proteinid = request.POST.get("proteinid")
    get_delete_protein(proteinid)
    return HttpResponse(f'Protein Deleted!')


def all_drugs(request): # 6.1
    drugs = get_drugs()
    return HttpResponse(str(drugs))
def all_proteins(request): # 6.2
    proteins = get_proteins()
    return HttpResponse(str(proteins))
def all_sides(request): #6.3
    sides = get_sides()
    return HttpResponse(str(sides))
def all_interactions(request): #6.4
    interactions = get_interactions()
    return HttpResponse(str(interactions))
def all_papers(request): #6.5
    papers = get_papers()
    return HttpResponse(str(papers))
def all_users(request): #6.6
    users = get_users()
    return HttpResponse(str(users))

def user_view(request):
    x = get_user_views()
   # x = [[j for j in i] for i in x]
    c1,c2,c3,c4,c5,c6 = [], [], [], [], [], []
    for row in x:
        c1.append(row[0])
        c2.append(row[1])
        c3.append(row[2])
        c4.append(row[3])
        c5.append(row[4])
        c6.append(row[5])
    columns = {"drug ids":str(c1), "drug names": str(c2), "smiles":str(c3), "descriptions":str(c4),"targetnames": str(c5), "side effect names":str(c6)}
    return JsonResponse(columns, safe=False)

def druglink1(request): #9
    drugid = request.POST.get("drugid")
    x = drug_helper1(drugid)
    return HttpResponse(str(x))

def druglink2(request): # 10
    drugid = request.POST.get("drugid")
    x = drug_helper2(drugid)
    return HttpResponse(str(x))

def druglink3(request): #11
    drugid = request.POST.get("drugid")
    x = drug_helper3(drugid)
    return HttpResponse(str(x))

def protein_interacting(request): #12
    proteinid = request.POST.get("proteinid")
    x = get_interacting_drugs_of_protein(proteinid)
    return HttpResponse(str(x))


def drugs_affecting_same_protein(request): #13
    x = get_drugs_affecting_same_protein()
    return HttpResponse(str(x))

def proteins_binding_same_drug(request): #14
    x = get_proteins_binding_same_drug()
    return HttpResponse(str(x))

def drugs_with_side_effect(request): #15
    umls_cui = request.POST.get("umls_cui")
    x = get_drugs_with_side_effect(umls_cui)
    return HttpResponse(str(x))

def search_description(request):
    keyword = request.POST.get("keyword")
    x = get_search_description(keyword)
    return HttpResponse(str(x))

def find_least_side(request): #17
    proteinid = request.POST.get("proteinid")
    x = get_find_least_side(proteinid)
    return HttpResponse(str(x))

def doi_authors(request): #18
    x = get_doi_authors()
    return HttpResponse(str(x))

def ranking(request):
    x = get_ranking()
    return render(request, 'show.html', x)

def add_author(request):
    author = request.POST.get("author")
    reactionid = request.POST.get("reactionid")
    get_add_author(author, reactionid)
    return HttpResponse("Author added!")

def home(request):
    if not 'status' in request.session:
        return redirect('../login')

    status = request.session['status']
    if status is None:
        return redirect('../login')
    is_manager = False
    is_not_manager = True
    if status == "manager":
        is_manager = True
        is_not_manager = False

    context = {
        "is_manager": is_manager,
        "is_not_manager": is_not_manager,
        "add_user_form": AddUserForm(),
        "drug_form": DrugIDForm(),
        "affinity_form": AffinityForm(),
        "protein_form": ProteinForm(),
        "umls_cui_form": UMLS_CUIForm(),
        "search_description": SearchDescriptionForm(),
        "authors_form": AuthorsForm()

    }

    return render(request, 'home.html', context)
