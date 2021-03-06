# Generated by Django 3.0.8 on 2020-11-12 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('sid', models.IntegerField()),
                ('name', models.CharField(max_length=60)),
                ('strength', models.IntegerField()),
                ('typeOfSchool', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=100)),
                ('achievements', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('contactInfo', models.IntegerField()),
                ('enteredBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
