from .models import Link

def ctk_Social(request):
    ctk_dict = {}
    links = Link.objects.all()

    for link in links:
        ctk_dict[link.chave] = link.url
    return ctk_dict

