# Generated by Django 3.2.9 on 2021-11-13 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bubble',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group', models.CharField(max_length=255)),
                ('radius', models.SmallIntegerField(default=1)),
                ('citing_patents_count', models.SmallIntegerField(default=1)),
            ],
        ),
    ]
