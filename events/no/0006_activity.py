# Generated by Django 2.2 on 2019-04-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('activity_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('event_id', models.BigIntegerField()),
                ('author_id', models.BigIntegerField()),
                ('activity_status_id', models.BigIntegerField()),
                ('title', models.TextField(max_length=200)),
                ('type', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('duration', models.DateField()),
            ],
        ),
    ]
