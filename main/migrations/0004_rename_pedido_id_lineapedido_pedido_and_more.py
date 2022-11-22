# Generated by Django 4.1.3 on 2022-11-21 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_pedido_lineapedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='lineapedido',
            old_name='producto_id',
            new_name='producto',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]