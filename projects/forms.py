from django import forms
from models import Product

class ProductForm(forms.ModelForm):
#size = forms.CharField(widget=CheckboxInput)

class Meta:
	model = Project
	fields = ('name', 'organization', 'description', 'email', 'image')