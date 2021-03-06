# Generated by Django 3.1.5 on 2021-03-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('t_person', models.IntegerField()),
                ('leads', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Form2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=2)),
                ('gender', models.CharField(max_length=6)),
                ('members', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=2)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
