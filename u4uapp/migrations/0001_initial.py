# Generated by Django 3.2.12 on 2022-10-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('tipo', models.CharField(max_length=128)),
                ('comuna', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('estudiantes', models.IntegerField()),
                ('fundacion', models.IntegerField()),
            ],
        ),
    ]
