# Generated by Django 2.2 on 2019-05-02 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20190502_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='answer_1',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='registration.Question_1'),
        ),
        migrations.AlterField(
            model_name='person',
            name='answer_2',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='registration.Question_2'),
        ),
    ]
