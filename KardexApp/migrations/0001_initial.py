# Generated by Django 4.2.5 on 2023-10-02 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.FloatField(default=0.0)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KardexApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(null=True)),
                ('cantidad', models.FloatField(default=0.0)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KardexApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(null=True)),
                ('cantidad', models.FloatField(default=0.0)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KardexApp.producto')),
            ],
        ),
    ]
