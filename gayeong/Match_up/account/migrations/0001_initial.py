# Generated by Django 3.1.1 on 2020-10-18 17:37

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('f_region', models.CharField(choices=[('경기', '경기도'), ('강원', '강원도'), ('경북', '경상북도'), ('경남', '경상남도'), ('충북', '충청북도'), ('충남', '충청남도'), ('전북', '전라북도'), ('전남', '전라남도'), ('제주', '제주도')], max_length=7)),
                ('w_region', models.CharField(choices=[('선택없음', '시, 도를 먼저 선택해주세요')], max_length=7)),
                ('my_team', models.CharField(default='무', max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
