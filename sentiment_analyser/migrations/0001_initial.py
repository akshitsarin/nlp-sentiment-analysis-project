# Generated by Django 3.0.8 on 2020-12-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('positive', models.IntegerField()),
                ('negative', models.IntegerField()),
            ],
        ),
    ]
