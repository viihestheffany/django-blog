from django import forms
from django.contrib.auth import get_user_model
User = get_user_model() # obtém o model padrão para usuários do Django

class AccountSignupForm(forms.ModelForm): # define um formulário para registro
  password = forms.CharField(label="Senha", max_length=50,
  widget=forms.PasswordInput())

  class Meta:
    model = User 
    fields = ('username', 'email', 'data_nascimento', 'cpf','password', ) 
    widgets = { 
      'data_nascimento': forms.widgets.DateInput(
         attrs={'type': 'date', 'required': 'required'}
),
}
