# Generated by Django 4.0.1 on 2022-02-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_taskemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskemail',
            name='email_prev_sent_at',
            field=models.IntegerField(default=0),
        ),
    ]