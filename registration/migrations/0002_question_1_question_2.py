# Generated by Django 2.2 on 2019-05-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_1', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_1', models.IntegerField()),
            ],
        ),
    ]
