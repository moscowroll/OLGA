# Generated by Django 2.2 on 2019-05-02 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20190502_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='answer_1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registration.Question_1'),
        ),
        migrations.AddField(
            model_name='person',
            name='answer_2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registration.Question_2'),
        ),
    ]
