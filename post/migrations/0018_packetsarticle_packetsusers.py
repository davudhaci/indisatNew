# Generated by Django 3.0.7 on 2020-10-10 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0017_delete_packetsusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacketsUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packet', models.CharField(choices=[('nrml', 'Normal'), ('vip', 'VIP'), ('dmnd', 'DIAMOND'), ('pre', 'PREMIUM')], default='Normal', max_length=50, verbose_name='Paketler')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Isdifadeci')),
            ],
        ),
        migrations.CreateModel(
            name='PacketsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packet', models.CharField(choices=[('nrml', 'Normal'), ('vip', 'VIP'), ('dmnd', 'DIAMOND'), ('pre', 'PREMIUM')], default='Normal', max_length=50, verbose_name='Paketler')),
                ('elan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Article', verbose_name='Elan')),
            ],
        ),
    ]