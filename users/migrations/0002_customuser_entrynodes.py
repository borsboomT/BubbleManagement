# Generated by Django 3.2.9 on 2021-11-12 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='entryNodes',
            field=models.ManyToManyField(blank=True, null=True, related_name='userEntries', to='nodes.Node'),
        ),
    ]