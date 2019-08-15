# Generated by Django 2.2.4 on 2019-08-15 06:25

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
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('group_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('group_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'PENDING'), ('a', 'ACCEPTED'), ('r', 'REFUSE')], max_length=1)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='users.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='기본프로필.png', upload_to='profile_pics')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('nickname', models.CharField(blank=True, max_length=30, null=True)),
                ('group', models.ManyToManyField(related_name='people', through='users.GroupMember', to='users.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='groupmember',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='users.Profile'),
        ),
    ]
