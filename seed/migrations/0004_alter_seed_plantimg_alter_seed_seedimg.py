# Generated by Django 5.0.1 on 2024-01-26 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0003_alter_seed_plantimg_alter_seed_seedimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='plantImg',
            field=models.ImageField(default='default_plant_pic.jpeg', upload_to='plant_pics'),
        ),
        migrations.AlterField(
            model_name='seed',
            name='seedImg',
            field=models.ImageField(default='default_seed_pic.PNG', upload_to='seed_pics'),
        ),
    ]