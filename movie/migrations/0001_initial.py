# Generated by Django 4.0 on 2022-04-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('director', models.CharField(max_length=256)),
                ('cast', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('duration_min', models.PositiveIntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]