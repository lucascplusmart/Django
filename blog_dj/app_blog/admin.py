from django.contrib import admin
from .models import Post, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','published','status')
    search_fields = ('title','content')
    list_filter = ('status','created','published','author')
    raw_id_fields = ('author', )
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'published'
    readonly_fields = ('visualizar_imagem',)

    def visualizar_imagem(self,obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem cadastrada"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created','published')
    search_fields = ('name',)
    list_filter = ('name','created','published')
    date_hierarchy = 'published'