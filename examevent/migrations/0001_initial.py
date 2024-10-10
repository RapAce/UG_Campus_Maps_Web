# Generated by Django 2.0.1 on 2018-05-24 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursetitle', models.CharField(max_length=120)),
                ('coursecode', models.CharField(max_length=120)),
                ('date', models.DateField()),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('college', models.CharField(max_length=120)),
                ('school', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=120)),
                ('level', models.IntegerField(default=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('venue', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='venue.Venue')),
            ],
        ),
    ]
