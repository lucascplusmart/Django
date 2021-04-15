from django.contrib import admin
from .models import Category, Product ,Images

# Register your models here.
# @admin.register(Category)

#admin.site.register(Category)
#admin.site.register(Product)
admin.site.register(Images)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent', 'status']
    list_filter = ['status']


#não precisa de decorador, pois atuar em outra classe(product).
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','status','image_tag']
    #list_display = ['title','category','status']
    list_filter = ['category']
    readonly_fields = ('image_tag',) # Nomes de modelos e métodos de administração de modelos só serão usados ​​se estiverem listados em readonly_fields.
    inlines = [ProductImageInline,]

#admin.site.register(Category,CategoryAdmin)
#admin.site.register(Product,ProductAdmin)