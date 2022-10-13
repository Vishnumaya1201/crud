# Generated by Django 4.1.2 on 2022-10-09 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=225)),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=225)),
                ('std_address', models.CharField(max_length=225)),
                ('std_age', models.IntegerField()),
                ('Join_date', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='capp.course')),
            ],
        ),
    ]
