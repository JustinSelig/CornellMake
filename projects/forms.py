from django import forms
from models import ProjectSubmission

class ProjectSubmissionForm(forms.ModelForm):
	#size = forms.CharField(widget=CheckboxInput)
	description = forms.CharField(widget=forms.Textarea)
	
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(ProjectSubmissionForm, self).__init__(*args, **kwargs)
		self.fields['description'].widget = forms.Textarea(attrs={
			'placeholder':'Idea Description',
			'rows':'3'}
		)

	class Meta:
		model = ProjectSubmission
		fields = ('name', 'email', 'organization', 'website', 'idea_name', 'description', 'category', 'image', 'url')