# Generated by Django 5.0.1 on 2024-01-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0006_delete_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='seedName',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
