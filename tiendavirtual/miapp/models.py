from django.db import models

# Create your models here.
# categorias
class categoria(models.Model):
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="cat_imga/")

    def __str__(self):
        return self.titulo

# marca del producto
class Marca(models.Model):
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="Marca_imga/")

    def __str__(self):
        return self.titulo

# modelo del producto
class producto(models.Model):
    Titulo=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to="producto_imga/")
    Detalles=models.TextField()
    Especificaciones=models.TextField()
    Precio=models.PositiveIntegerField()
    Categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)
    Marca=models.ForeignKey(Marca,on_delete=models.CASCADE)
    Estado=models.BooleanField(default=True)

    def __str__(self):
        return self.Titulo