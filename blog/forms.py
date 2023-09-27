# Python
from datetime import datetime

# Django
from django import forms

# Local
from blog.models import Post # importa o model Post


# Cria o ModelForm herdando da classe base - *Respeite a indentação*.

class PostModelForm(forms.ModelForm):
  error_css_class = 'alert-danger'
  
  def __init__(self, *args, **kwargs):
    super(PostModelForm, self).__init__(*args, **kwargs)
# Configura um valor inicial para o campo pub_date
    self.fields['pub_date'].initial = datetime.today()
  
  class Meta: 
    model = Post
    fields = ('body_text', 'pub_date', 'categoria')
    widgets = {
      'pub_date': forms.widgets.DateInput(attrs={'type': 'date'}),
      'categoria': forms.RadioSelect(),
    }
    labels = { 'body_text': '', 'categoria': 'Assunto'}

  def clean(self):
    cleaned_data = super().clean() 
    pub_date = cleaned_data.get('pub_date') 
    pub_date = pub_date.replace(tzinfo=None)
    
    if pub_date > datetime.today():
      self.add_error(
        'pub_date',
        forms.ValidationError('Não é permitido datas futuras')
)