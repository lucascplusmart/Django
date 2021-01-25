# Create your views here.

'''
Uma view é um “tipo” de página Web em sua aplicação Django que em geral serve a uma função específica e tem um template específico. 
Por exemplo, 

=> em uma aplicação de blog, você deve ter as seguintes views:

    -Página inicial do blog - exibe os artigos mais recentes.
    -Página de “detalhes” - página de vínculo estático permanente para um único artigo.
    -Página de arquivo por ano - exibe todos os meses com artigos para um determinado ano.
    -Página de arquivo por mês - exibe todos os dias com artigos para um determinado mês.
    -Página de arquivo por dia - exibe todos os artigos de um determinado dia.
    -Ação de comentários - controla o envio de comentários para um artigo.
    -Em nossa aplicação de enquetes, nós teremos as seguintes views:

Página de “índice” de enquetes - exibe as enquetes mais recente.
Question “detail” page – displays a question text, with no results but with a form to vote.
Página de “resultados” de perguntas - exibe os resultados de uma pergunta em particular.
Ação de voto - gerencia a votação para uma escolha particular em uma enquete em particular.'''

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

from django.urls import reverse

from django.views import generic

from .models import Question, Choice

from django.utils import timezone


#from django.template import loader
#from django.http import Http404

# views genéricas: Menos código é melhor
"""
Nas partes anteriores deste tutorial, os templates tem sido fornecidos com um contexto que contém as variáveis question e latest_question_list. Para a DetailView a variavel question é fornecida automaticamente – já que estamos usando um modelo Django (Question), Django é capaz de determinar um nome apropriado para a variável de contexto. Contudo, para ListView, a variável de contexto gerada automaticamente é question_list. Para sobrescrever nós fornecemos o atributo context_object_name, especificando que queremos usar latest_question_list no lugar. Como uma abordagem alternativa, você poderia mudar seus templates para casar o novo padrão das variáveis de contexto – mas é muito fácil dizer para o Django usar a variável que você quer.
"""
class IndexView(generic.ListView):
    template_name = 'polls/home.html'
    context_object_name = 'latest_question_list'
    '''
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]'''
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now() 
            ).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

=> isto é equivalente a função index acima

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context
'''

'''
def detail(request, question_id): # cada função é uma pagina web
    return HttpResponse("You're looking at question %s." % question_id)'''


'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})'''
    

#=> metodo paythonic de levnatar as erro 404
'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) ''' 

'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question}) '''




'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#Esta é a view mais simples possível no Django. Para chamar a view, nós temos que mapear a URL 
# - e para isto nós precisamos de uma URLconf.
#Para criar uma URLconf no diretório polls, crie um arquivo chamado urls.py'''
