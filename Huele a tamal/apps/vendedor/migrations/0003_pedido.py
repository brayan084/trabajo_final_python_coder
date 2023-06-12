# Generated by Django 4.2.1 on 2023-06-12 06:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
        ('vendedor', '0002_alter_vendedor_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('fecha_venta', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Productos.producto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendedor.vendedor')),
            ],
        ),
    ]
