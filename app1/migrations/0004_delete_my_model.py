# Generated by Django 4.2 on 2023-04-20 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_my_model_age_alter_my_model_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='My_Model',
        ),
    ]