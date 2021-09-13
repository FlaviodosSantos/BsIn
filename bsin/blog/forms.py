from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class CadastroUsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True,
                            help_text='Obrigatório. O maximo é 30 caracteris. '
                                        'Letras minúsculas, números e @ . + - _ apenas.')
    email = forms.EmailField(max_length=254, required=True, help_text='Obrigatório. Informe um e-mail válido.')

    foto = forms.ImageField(required=False, help_text='A foto é opcional')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','foto')

