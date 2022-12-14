# Generated by Django 4.0.4 on 2022-09-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0017_student_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_feedback',
            name='Updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff_feedback',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_feedback',
            name='Updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_feedback',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
