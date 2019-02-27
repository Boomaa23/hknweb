# Generated by Django 2.1.5 on 2019-02-04 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hknweb', '0006_profile_email'),
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offchallenge',
            options={'verbose_name': 'Officer challenge'},
        ),
        migrations.AddField(
            model_name='offchallenge',
            name='requester',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='hknweb.Profile'),
        ),
        migrations.AlterField(
            model_name='offchallenge',
            name='officer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='officer', to='hknweb.Profile'),
        ),
    ]
