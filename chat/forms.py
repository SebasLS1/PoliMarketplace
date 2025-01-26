from django.forms import ModelForm
from django import forms
from .models import ChatMessage

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'class': 'p-4 text-black',
                'placeholder': 'Escribe tu mensaje...',
                'autofocus': True,
                'maxlength': 300,
                'style': 'width: 680px;'  
                
            })
        }