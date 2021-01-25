from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    send = False
    
    form = ContactForm(request.POST or None)

    if form.is_valid():
        nome = request.POST.get('nome','')
        email = request.POST.get('email','')
        mensagem = request.POST.get('mensagem','')

        email=EmailMessage(
            "Mensagem do blog django",
            "de {} <{}>.Escreveu:\n\n {}".format(nome,email,mensagem),
            "nao-responder@inbox.mailtrap.io",
            ["lucascplusmart@gmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
        except:
            send = False

        send = True
    
    context = {
        'form':  form,
        'success': send
    }
    return render(request,'contact/contact.html',context)
