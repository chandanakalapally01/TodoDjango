# Generated by Django 3.2.3 on 2021-06-09 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]
