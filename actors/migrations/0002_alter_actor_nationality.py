# Generated by Django 5.1.4 on 2025-02-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('BRA', 'Brasil'), ('USA', 'Estados Unidos'), ('CHN', 'China'), ('RUS', 'Russia'), ('JPN', 'Japão'), ('UK', 'Reino Unido')], max_length=100, null=True),
        ),
    ]
