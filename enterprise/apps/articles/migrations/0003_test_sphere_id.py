# Generated by Django 2.2.7 on 2019-12-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_group_subject_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='sphere_id',
            field=models.CharField(max_length=20, null=True, verbose_name='ID завдання в sphere engine'),
        ),
    ]