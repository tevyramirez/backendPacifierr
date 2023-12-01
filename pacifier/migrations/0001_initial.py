# Generated by Django 4.2.7 on 2023-11-16 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('observacion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreditoProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprobante', models.CharField(max_length=100)),
                ('proveedor', models.CharField(max_length=255)),
                ('fecha_compra', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_vencimiento1', models.DateField()),
                ('cuota1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_vencimiento2', models.DateField()),
                ('cuota2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_vencimiento3', models.DateField()),
                ('cuota3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_vencimiento4', models.DateField()),
                ('cuota4', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_vencimiento5', models.DateField()),
                ('cuota5', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=25)),
                ('ci', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_ingreso', models.DateField()),
                ('estado_civil', models.CharField(max_length=10)),
                ('login', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=100)),
                ('modulo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=25)),
                ('razon_social', models.CharField(max_length=255)),
                ('representante', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('dias_credito', models.IntegerField()),
                ('fecha_ingreso', models.DateField()),
                ('observacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubcategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategoria', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=125)),
                ('descripcion', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.categoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=100)),
                ('unidad', models.CharField(max_length=10)),
                ('stock', models.IntegerField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ganancia', models.IntegerField()),
                ('valor_ganancia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('val_iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField()),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.subcategoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_descuento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_pago', models.CharField(max_length=10)),
                ('efectivo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deuda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.CharField(max_length=20)),
                ('fecha_compra', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_descuento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_pago', models.CharField(max_length=10)),
                ('efectivo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deuda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.empleado')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedidoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('unidad', models.CharField(max_length=10)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.IntegerField()),
                ('valor_descuento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.pedidoventa')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedidoCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('unidad', models.CharField(max_length=10)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.IntegerField()),
                ('valor_descuento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.pedidocompra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePagoProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.CharField(max_length=255)),
                ('cuota', models.IntegerField()),
                ('fecha_pago', models.DateTimeField()),
                ('abono', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('credito_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.creditoproveedor')),
            ],
        ),
        migrations.AddField(
            model_name='creditoproveedor',
            name='cab_pedido_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacifier.pedidocompra'),
        ),
    ]
