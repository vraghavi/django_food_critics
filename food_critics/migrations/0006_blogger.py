# Generated by Django 3.2.9 on 2021-11-17 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_critics', '0005_auto_20211106_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.TextField(max_length=20)),
                ('mobileno', models.TextField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_critics.user')),
            ],
        ),
    ]
