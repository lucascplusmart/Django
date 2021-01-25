from django import  forms

class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome',widget=forms.TextInput(attrs={"placeholder":'Digite seu nome'}))
    email = forms.EmailField(label='E-mail',widget=forms.TextInput(attrs={"placeholder":'Digite seu E-mail'}))
    mensagem = forms.CharField(label='Assunto',widget=forms.Textarea(attrs={"placeholder":'Assunto'}))
