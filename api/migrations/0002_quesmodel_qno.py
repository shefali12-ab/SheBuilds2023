# Generated by Django 4.1.5 on 2023-01-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='qno',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
