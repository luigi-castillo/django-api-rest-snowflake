# Generated by Django 4.1.7 on 2023-03-10 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('department', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('job', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HiredEmployees',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.departments')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.jobs')),
            ],
        ),
    ]
