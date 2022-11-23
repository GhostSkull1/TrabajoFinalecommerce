from django.contrib import admin
from .models import categoria,Marca,producto
# Register your models here.

# registro de los modelos productos
admin.site.register(categoria)
admin.site.register(Marca)

class ProductoAdmin(admin.ModelAdmin):
    list_display=('id','Titulo','Marca','Precio','Estado') # organizar el producto en el admin de django
    list_editable=('Estado',)  # quitar o poner chulito del producto
admin.site.register(producto,ProductoAdmin)


#admin.site.register(ProductoAdmin)