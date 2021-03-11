# Generated by Django 3.0.5 on 2021-03-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Segment', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Product', models.CharField(max_length=100)),
                ('Sales', models.IntegerField(max_length=100)),
                ('Units', models.IntegerField(max_length=100)),
                ('Datesold', models.CharField(max_length=100)),
            ],
        ),
    ]
