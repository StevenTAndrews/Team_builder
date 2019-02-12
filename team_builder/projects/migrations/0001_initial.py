# Generated by Django 2.1.5 on 2019-02-11 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Application')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('skill', models.CharField(blank=True, choices=[('Android', 'Android Developer'), ('Design', 'Designer'), ('Java', 'Java Developer'), ('PHP', 'PHP Developer'), ('Python', 'Python Developer'), ('Rails', 'Rails Developer'), ('Wordpress', 'Wordpress Developer'), ('iOS', 'iOS Developer')], default='', max_length=20)),
                ('position_filled', models.BooleanField(blank=True, default=False)),
                ('applicants', models.ManyToManyField(through='projects.Application', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('timeline', models.CharField(max_length=255)),
                ('requirements', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='application',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Position'),
        ),
    ]
