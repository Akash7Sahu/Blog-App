# Generated by Django 2.2 on 2019-05-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20190509_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('pic', models.FileField(upload_to='images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Bbb',
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
