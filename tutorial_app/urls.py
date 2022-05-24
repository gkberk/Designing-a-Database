from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('<int:num>', views.printnum, name='printnum'),
    path('<str:string>/string', views.printstring, name='printstring'),

    path('login/', views.loginfirst, name='loginfirst'),
    path('login/#', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('adduser/', views.add_user, name='adduser'),
    path('drugpage/', views.drug_page, name='opendrugpage'),
    path('delete-drug/', views.delete_drug, name='delete-drug'),
    path('update-affinity/', views.update_affinity, name='update-affinity'),
    path('delete-protein/', views.delete_protein, name='delete-protein'),
    path('alldrugs/', views.all_drugs, name='alldrugs'),
    path('allproteins/', views.all_proteins, name='allproteins'),
    path('allsides/', views.all_sides, name='allsides'),
    path('alldrugs/', views.all_drugs, name='alldrugs'),
    path('allinteractions/', views.all_interactions, name='allinteractions'),
    path('allpapers/', views.all_papers, name='allpapers'),
    path('allusers/', views.all_users, name='allusers'),
    path('userview/', views.user_view, name='userview'),
    path('druglink1/', views.druglink1, name='druglink1'),
    path('druglink2/', views.druglink2, name='druglink2'),
    path('druglink3/', views.druglink3, name='druglink3'),
    path('proteininteracting', views.protein_interacting, name='proteininteracting'),
    path('drugs-affecting-same-protein', views.drugs_affecting_same_protein, name='drugs-affecting-same-protein'),
    path('proteins-binding-same-drug', views.proteins_binding_same_drug, name='proteins-binding-same-drug'),
    path('drugs-with-side-effect', views.drugs_with_side_effect, name='drugs-with-side-effect'),
    path('search-description', views.search_description, name='search-description'),
    path('find-least-side', views.find_least_side, name='find-least-side'),
    path('doi-authors', views.doi_authors, name='doi-authors'),
    path('ranking', views.ranking, name='ranking'),
    path('add-author', views.add_author, name='add-author')
]


