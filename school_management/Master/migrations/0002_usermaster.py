# Generated by Django 3.0 on 2019-12-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
    ]