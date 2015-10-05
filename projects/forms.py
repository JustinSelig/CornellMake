from django import forms
from models import ProjectSubmission

class ProjectSubmissionForm(forms.ModelForm):
	#size = forms.CharField(widget=CheckboxInput)
	description = forms.CharField(widget=forms.Textarea)
	
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(ProjectSubmissionForm, self).__init__(*args, **kwargs)
		
#		self.fields['description'].widget = forms.Textarea(attrs={
#			'placeholder':'Idea Description',
#			'rows':'3'}
#		)

	def save(self, commit=True):
		instance = super(ProjectSubmissionForm, self).save(commit=False)
		instance.owner = self.request.user
		
		if commit:
			instance.save()
		return instance

	class Meta:
		model = ProjectSubmission
		fields = ('name', 'email', 'organization', 'website', 'idea_name', 'description', 'category', 'image', 'url')