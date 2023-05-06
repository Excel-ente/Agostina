# Generated by Django 3.2.18 on 2023-04-30 23:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cotizador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticuloOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_receta', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('cantidad', models.DecimalField(decimal_places=2, default=1, max_digits=20)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('fecha_ultimo_costo', models.DateField(blank=True, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('ganancia', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CierreCaja',
            fields=[
                ('numero_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=datetime.datetime.now, unique=True)),
                ('efectivo_inicial', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('efectivo_final', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_ventas', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('gastos', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('pagos_clientes', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('retiros_efectivo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('final', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('diferencias', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cierre de Caja',
                'verbose_name_plural': 'Cierres de Caja',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('NUMERO_CLIENTE', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE_Y_APELLIDO', models.CharField(max_length=120)),
                ('EMAIL', models.CharField(blank=True, max_length=120, null=True)),
                ('TELEFONO', models.CharField(blank=True, max_length=15, null=True)),
                ('PEDIDOS_TOTALES', models.IntegerField(blank=True, default=0, null=True)),
                ('PEDIDOS_ENTREGADOS', models.IntegerField(blank=True, default=0, null=True)),
                ('PEDIDOS_PENDIENTES', models.IntegerField(blank=True, default=0, null=True)),
                ('FECHA_PROXIMA_ENTREGA', models.DateField(blank=True, null=True)),
                ('COMENTARIOS', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ESTADO', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('codigo_gasto', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('pago', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('detalle', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('adelanto', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('debe', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('aclaraciones', models.CharField(blank=True, max_length=255, null=True)),
                ('articulos', models.ManyToManyField(through='administracion.ArticuloOrden', to='cotizador.Receta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.cliente')),
                ('estado', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.estado')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Retiro',
            fields=[
                ('codigo_retiro', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('detalle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('codigo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('total_orden', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('pago', models.DecimalField(decimal_places=2, max_digits=20)),
                ('deuda_pendiente', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.cliente')),
                ('orden_asociada', models.ForeignKey(limit_choices_to=models.Q(('debe__gt', 0)), on_delete=django.db.models.deletion.CASCADE, to='administracion.orden')),
            ],
            options={
                'verbose_name': 'Pagos de Clientes',
                'verbose_name_plural': 'Pagos de Clientes',
            },
        ),
        migrations.AddField(
            model_name='articuloorden',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.orden'),
        ),
        migrations.AddField(
            model_name='articuloorden',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizador.receta'),
        ),
    ]