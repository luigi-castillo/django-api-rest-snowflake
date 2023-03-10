# Generated by Django 4.1.7 on 2023-03-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_departments_department_alter_departments_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='department',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='departments',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hiredemployees',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='hiredemployees',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job',
            field=models.TextField(null=True),
        ),
    ]
