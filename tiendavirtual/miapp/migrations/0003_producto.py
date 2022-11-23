# Generated by Django 4.1.3 on 2022-11-23 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='producto_imga/')),
                ('Detalles', models.TextField()),
                ('Especificaciones', models.TextField()),
                ('Precio', models.PositiveIntegerField()),
                ('Estado', models.BooleanField(default=True)),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.categoria')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.marca')),
            ],
        ),
    ]