# Generated by Django 3.1.2 on 2020-11-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('user', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]