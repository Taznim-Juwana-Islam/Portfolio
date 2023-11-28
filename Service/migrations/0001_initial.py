# Generated by Django 4.2.4 on 2023-10-11 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_title', models.CharField(max_length=10)),
                ('website_description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.FileField(default=None, max_length=250, null=True, upload_to='news/')),
                ('status', models.TextField()),
            ],
        ),
    ]