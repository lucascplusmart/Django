#from django.shortcuts import render

#from django.http import HttpResponse , HttpResponseRedirect

#from django.views.generic import ListView

from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin

from .models import Setting

from .forms import ContactForm ,ContactMessage


from django.urls import reverse_lazy

# Create your views here.

# http://127.0.0.1:8000



class  EshopListView(generic.ListView):
    model = Setting
    template_name= 'home/home.html'
    # por padrão o nome do objeto é "object" logo a instrução a baixo muda o nome do obejto
    context_object_name = 'setting' 
    def get_queryset(self):
        return Setting.objects.get(status=True)
    

# vai herda EshopListView => generic.ListView
class  EshopAboutusView(EshopListView):
    template_name= 'home/about.html'
   


# vai herda EshopListView => generic.ListView
class  EshopContactusView(SuccessMessageMixin,EshopListView,generic.FormView):
    template_name= 'home/contact.html'
    form_class = ContactForm
    fil = None
    success_url = reverse_lazy('contactus')
    #success_message = "mensangem enviada com sucesso!"

    """
    success_message = "%(field)s - mensangem enviada com sucesso!"
    # função para maniupular a menssagem 
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field = None,
        )"""
    def form_valid(self,form):
        obj = form.save(commit=False)
        #obj.author = self.request.user
        obj.ip = self.request.META.get('REMOTE_ADDR')
        obj.save()
        return super().form_valid(form)

   





  


'''

def  EshopContactusView(request):
    setting = Setting.objects.get(pk=1)
    context={'setting':setting }
    return render(request, 'home/contact.html', context)


class  EshopContactusView(generic.ListView):
    model = Setting
    template_name= 'home/contact.html'

def EshopListView(request):
    return render(request,'home/home.html')

def  EshopAboutus(request):
    return HttpResponse("my aboutus page")


def  EshopContactus(request):
    return HttpResponse("my contact page")

'''