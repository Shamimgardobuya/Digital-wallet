# Generated by Django 4.2.1 on 2023-06-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_type',
            field=models.CharField(choices=[('Mshwari', 'Mshwari'), ('fuliza', 'fuliza')], max_length=10, null=True),
        ),
    ]