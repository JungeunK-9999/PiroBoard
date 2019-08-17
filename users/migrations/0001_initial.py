# Generated by Django 2.2.4 on 2019-08-17 04:46

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
                ('group_apply_status', models.CharField(choices=[('n', '가입 신청 비허용'), ('y', '가입 신청 허용')], default='y', max_length=1)),
                ('group_open_status', models.CharField(choices=[('n', '비공개'), ('s', '검색만가능'), ('o', '공개')], default='o', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('g', '가입요청'), ('u', '가입승인요청'), ('a', 'ACCEPTED'), ('r', 'REFUSE')], max_length=1)),
                ('group_role', models.CharField(choices=[('h', '그룹장'), ('m', '그룹 멤버')], default='m', max_length=1)),
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
                ('group', models.ManyToManyField(blank=True, null=True, related_name='groups', through='users.GroupMember', to='users.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='groupmember',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='group',
            name='group_users',
            field=models.ManyToManyField(related_name='people', through='users.GroupMember', to='users.Profile'),
        ),
    ]
