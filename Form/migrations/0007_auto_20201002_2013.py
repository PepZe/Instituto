# Generated by Django 3.1.1 on 2020-10-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0006_auto_20201002_0011'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teste',
        ),
        migrations.AddField(
            model_name='register',
            name='phone',
            field=models.CharField(default='(11)99954328', max_length=14),
            preserve_default=False,
        ),
    ]
