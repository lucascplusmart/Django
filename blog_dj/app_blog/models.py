from django.db import models
from  django.utils import  timezone
from django.contrib.auth.models import User
from django.urls import  reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import  receiver
from ckeditor.fields import RichTextField
from  django.utils.html import mark_safe

# Create your models here.

class  PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                            .filter(status="publicado")

class Category(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering= ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado','Publicado')
    )
    title = models.CharField(max_length=250, verbose_name="Título")
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    #content = models.TextField(verbose_name="Conteúdo")
    content = RichTextField(verbose_name="Conteúdo")
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status =models.CharField(max_length=10,choices=STATUS, default='rascunho')
    image = models.ImageField(upload_to="blog",blank=True, null=True)

    category = models.ManyToManyField(Category,related_name="get_posts" )
    @property
    def view_image(self):
        return mark_safe('<img src="%s" width = "400px" /> ' %self.image.url)
    
    class Meta:
        ordering = ('-published',)
        
   
    objects   = models.Manager()
    publishedManager = PublishedManager()
    # url absoluta
    def get_absolute_url(self):
        #return reverse('detail',args=[self.pk])
        return reverse('detail',args=[self.slug])
    
    def get_absolute_update(self):
        return reverse('post_edit',args=[self.slug])
        #return reverse('post_edit',args=[self.pk])
    

    def get_absolute_delete(self):
        #return reverse('post_edits',args=[self.slug])
        return reverse('post_delete',args=[self.pk])
    

    def __str__(self):
        return self.title



@receiver(post_save,sender=Post)
def insert_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()