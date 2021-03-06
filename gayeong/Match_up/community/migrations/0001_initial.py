# Generated by Django 3.1.1 on 2020-10-20 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_auto_20201020_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='블로그 글의 분류를 입력하세요.(ex:일상)', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Community_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_image', models.ImageField(blank=True, upload_to='image')),
                ('content', models.TextField()),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
                ('category', models.ManyToManyField(help_text='글의 분류를 설정하세요.', to='community.Category')),
            ],
        ),
    ]
