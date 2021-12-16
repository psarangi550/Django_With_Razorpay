# Generated by Django 4.0 on 2021-12-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]