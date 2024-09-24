# Generated by Django 5.0.7 on 2024-09-23 07:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_1', to=settings.AUTH_USER_MODEL)),
                ('User_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('ChatRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ChatRoom', to='Chat.chatroom')),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver', to=settings.AUTH_USER_MODEL)),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
