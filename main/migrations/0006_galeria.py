# Generated by Django 4.1.3 on 2022-11-23 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_pedido_total_ped'),
    ]

    operations = [
        migrations.CreateModel(
            name='galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
