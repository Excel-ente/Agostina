# Generated by Django 3.2.18 on 2023-04-30 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRODUCTO', models.CharField(max_length=120)),
                ('DETALLE', models.TextField(blank=True, null=True)),
                ('STOCK', models.IntegerField(blank=True, default=0, null=True)),
                ('UNIDAD_MEDIDA_COMPRA', models.CharField(choices=[('Unidades', 'Unidades'), ('Kilogramos', 'Kilogramos'), ('Litros', 'Litros'), ('Onzas', 'Onzas'), ('Libras', 'Libras')], default='Unidades', max_length=10)),
                ('CANTIDAD', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('PRECIO_COMPRA', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('UNIDAD_MEDIDA_USO', models.CharField(choices=[('Unidades', 'Unidades'), ('Gramos', 'Gramos'), ('Mililitros', 'Mililitros'), ('Onzas', 'Onzas'), ('Libras', 'Libras')], default='Unidades', max_length=10)),
                ('COSTO_UNITARIO', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=120)),
                ('DETALLE', models.CharField(blank=True, max_length=120, null=True)),
                ('COSTO_RECETA', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=22, null=True)),
                ('GASTOS_ADICIONALES', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=22, null=True)),
                ('RENTABILIDAD', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('PRECIO_VENTA', models.DecimalField(decimal_places=2, default=1, max_digits=22)),
                ('COSTO_FINAL', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=22, null=True)),
                ('ULTIMA_ACTUALIZACION', models.DateTimeField(auto_now=True, null=True)),
                ('INGREDIENTES', models.ManyToManyField(to='cotizador.Insumo')),
            ],
            options={
                'verbose_name': 'Nuevo Producto',
                'verbose_name_plural': 'Lista de Precios',
            },
        ),
        migrations.CreateModel(
            name='ingredientereceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, default=1, max_digits=20)),
                ('costo_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('medida_uso', models.CharField(blank=True, max_length=255, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('pruducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizador.insumo')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizador.receta')),
            ],
        ),
    ]
