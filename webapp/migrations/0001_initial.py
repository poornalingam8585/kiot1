# Generated by Django 3.2.8 on 2023-03-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
    ]