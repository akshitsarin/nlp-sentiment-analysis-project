# Generated by Django 3.0.8 on 2020-12-29 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment_analyser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]
