# Generated by Django 5.1.4 on 2025-02-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_student_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='note',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
