# Generated by Django 4.0.4 on 2022-09-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0014_staff_feedback_feedback_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_feedback',
            name='feedback_reply',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]