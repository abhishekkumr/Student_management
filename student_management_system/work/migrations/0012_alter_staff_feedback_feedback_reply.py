# Generated by Django 4.0.4 on 2022-09-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_staff_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_feedback',
            name='feedback_reply',
            field=models.TextField(null=True),
        ),
    ]
