# Generated by Django 5.1.4 on 2025-01-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='num_studs',
        ),
        migrations.AddField(
            model_name='institution',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
