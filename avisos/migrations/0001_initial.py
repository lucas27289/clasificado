# Generated by Django 3.2.9 on 2021-11-24 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=False)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='assets/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='img/%y')),
                ('alt_text', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('nick', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avisos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='img/anuncios/%y')),
                ('id_anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avisos.anuncio')),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='id_categoria',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='avisos.categoria'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='id_subcategoria',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='avisos.subcategoria'),
        ),
    ]
