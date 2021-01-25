# Create your models here.
from django.db import models
from django.utils import timezone
import datetime
'''

=> Um modelo é a fonte única e definitiva de dados sobre os seus dados. 
Ele contém os campos e comportamentos essenciais dos dados que você está 
gravando. Geralmente, cada modelo mapeia para uma única tabela no banco de dados.

O Django segue o princípio DRY. (Não repita a si mesmo), redudancia é ruim, normalizar é bom


=> O objetivo é definir seu modelo de dados em um único local e automaticamente derivar coisas(exemplo: tabela) a partir dele.

 => O básico:

1º) Cada modelo é uma classe Python que extende django.db.models.Model.

2º) Cada atributo do modelo representa uma coluna do banco de dados.

3º)Com tudo isso, o Django lhe dá uma API de acesso a banco de dados gerada automaticamente, 
o que é explicado em Fazendo consultas.

'''

#exemplo:

'''

class Question(models.Model):
    # são campos do modelo. 
    # Cada campo é especificado como um atributo de classe, 
    # e cada atributo é mapeado para uma coluna no banco de dados.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

=> isso seria equivalente ao codigo PostgreSQL:

CREATE TABLE polls_question (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "question_text" varchar(200) NOT NULL
);

O nome da tabela, myapp_person, é automaticamente derivado de alguns metadados do modelo, no entanto isto pode ser sobrescrito.

Um campo id é adicionado automaticamente, mas esse comportamento também pode ser alterado.

O comando SQL CREATE TABLE nesse exemplo é formatado usando a sintaxe do PostgreSQL, 
mas é digno de nota que o Django usa o SQL adaptado ao banco de dados especificado no seu arquivo de configurações.

'''



class Question(models.Model):
    # são campos do modelo. 
    # Cada campo é especificado como um atributo de classe, 
    # e cada atributo é mapeado para uma coluna no banco de dados.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    """   
    Esta função tem um problema
    Se a publicação for no futuro a função retorna true.
    Desde que coisas no futuro não são ‘recent’, isto é claramente um erro.

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)"""
    '''
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now'''
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    # são campos do modelo. 
    # Cada campo é especificado como um atributo de classe, 
    # e cada atributo é mapeado para uma coluna no banco de dados.
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

'''
Finalmente, note que uma relação foi criada, usando ForeignKey(chave estrangeira). 
Isso diz ao Django que cada Choice está relacionada a uma única Question, mas cada questão pode ter varias choice.
O Django oferece suporte para todos os relacionamentos comuns de um banco de dados: muitos-para-um, muitos-para-muitos e um-para-um.

[Question] 1:1 ----(relação)---- 1:N  [Choice], 

 - toda questão há no minimo 1 altenativa e no maxmio varias alternativas
 - toda alternativa está no minimo em 1 questão e no maximo em 1 questão

'''