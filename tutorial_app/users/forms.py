from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))


class AddUserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Institution'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))


class DrugIDForm(forms.Form):
    drugid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'DrugID'}))


class DrugAffinityForm(forms.Form):
    drugaffinity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New Affinity'}))


class AffinityForm(forms.Form):
    reactionid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Reaction ID'}))
    affinity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New Affinity'}))


class ProteinForm(forms.Form):
    proteinid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New Protein'}))

class UMLS_CUIForm(forms.Form):
    umls_cui = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'UMLS_CUI'}))

class SearchDescriptionForm(forms.Form):
    keyword = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'keyword'}))

class AuthorsForm(forms.Form):
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'author'}))
    reactionid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'reactionid'}))


