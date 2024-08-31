# Generated by Django 5.0.7 on 2024-08-31 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Founding_date', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Description', models.TextField()),
                ('Founder', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['Company_name'],
            },
        ),
    ]
