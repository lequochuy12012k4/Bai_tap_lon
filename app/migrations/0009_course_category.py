# Generated by Django 5.1.6 on 2025-03-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_category_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(related_name='course', to='app.category'),
        ),
    ]
