# Generated by Django 3.1.4 on 2020-12-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomat_fwd_chaining', '0003_gejala_pilihan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gejala',
            name='pilihan',
            field=models.CharField(choices=[('benar', 'ini benar'), ('salah', 'ini salah')], default='salah', max_length=10),
        ),
    ]
