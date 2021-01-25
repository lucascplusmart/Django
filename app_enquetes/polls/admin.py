from django.contrib import admin

# Register your models here.
from .models import Question, Choice

'''
=>  admin.site.register(Question)
=> admin.site.register(Choice)
    
Ao registrarmos o modelo de Question através da linha admin.site.register(Question), 
o Django constrói um formulário padrão para representá-lo. Comumente, você desejará 
personalizar a apresentação e o funcionamento dos formulários do site de administração 
do Django. Para isto, você precisará informar ao Django as opções que você quer utilizar 
ao registrar o seu modelo.
'''



'''
Você seguirá este padrão – crie uma classe de “model admin”, 
em seguida, passe-a como o segundo argumento para o admin.site.register() 
– todas as vezes que precisar alterar as opções administrativas para um modelo.
'''    
#=> com o codigo abaixo, é posso escolher qual campo aprece primeiro

'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)'''

#=> com o codigo abaixo, você pode querer dividir o formulário em grupos
# O primeiro elemento de cada tupla em fieldsets é o título do grupo. Aqui está como o nosso formulário se parece agora:

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # O tipo do filtro apresentado depende do tipo do campo pelo qual você está filtrando
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


# => Com o TabularInline (em vez de StackedInline), 
# os objetos relacionados são exibidos de uma maneira mais compacta, formatada em tabela:

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
