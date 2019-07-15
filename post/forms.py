from django import forms 
from .models import Comment, Message

class commentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('writer','email','body')

class messageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('name','email','subject', 'body')