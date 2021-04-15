from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


# blank => Definindo blank=True você não obriga que o campo seja preenchido nos formulários, 
# podendo ficar em branco, se definir blank=False esse campo será obrigatório, isto é, não poderá ficar 
# em branco.


'''Se vc define null=True (o contrário de NOT NULL) em um campo de seu modelo (uma coluna do BD), 
ao entrar com valores em branco para tipos como DateTimeField e ForeignKey serão armazenados como NULL em
seu BD, isso é muito útil para as FKs, quando vc quer que o item relacionado possa ser deixado em branco.'''

#============================
# ps: colocar o slug de forma automatica

"""
funciona também assim, só que não tem muitas funcionalidades:

ckeditor em sttings.py/apps
from ckeditor.fields import RichText
detail = RichTextField(verbose_name="Conteúd

"""





class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS, default="False")
    slug = models.SlugField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #n:1, 1 produto em 1 cateoria / n produtos em 1 cateoria
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(blank=False,upload_to='images/')
    price = models.FloatField()
    amount=models.IntegerField()
    minamount=models.IntegerField()
    #detail=models.TextField()
    detail=RichTextUploadingField()
    slug = models.SlugField()
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    # maraca a strig como segura, isso quer dizer que a string já está no formato apropido para o html
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE) # n : 1. n imagaem par a 1 produto / 
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


