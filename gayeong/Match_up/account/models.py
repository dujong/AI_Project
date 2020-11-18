
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    first_region = [
        ('경기', '경기도'),
        ('강원', '강원도'),
        ('경북', '경상북도'),
        ('경남', '경상남도'),
        ('충북', '충청북도'),
        ('충남', '충청남도'),
        ('전북', '전라북도'),
        ('전남', '전라남도'),
        ('제주', '제주도'),
    ]

    two_region = [
        ('선택없음', '시, 도를 먼저 선택해주세요')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length = 13, unique = True)
    email = models.EmailField(null=True, blank=False, unique=True)
    phone = models.CharField(max_length = 11, unique = True)
    f_region = models.CharField(max_length = 7, choices = first_region)
    w_region = models.CharField(max_length = 7, choices = two_region, default = "시, 도를 먼저 선택해주세요")
    my_team = models.CharField(max_length = 16, default = "없음")

    def __str__(self):
        return self.user_name


'''
    if first_region == '경기도':
        two_region = [
            ('수원', '수원시'), ('성남', '성남시'), ('용인', '용인시'), ('안양', '안양시'),
            ('안산', '안산시'), ('과천', '과천시'), ('광명', '광명시'), ('광주', '광주시'),
            ('군포', '군포시'), ('부천', '부천시'),

        ]
    elif first_region == '강원도':
        two_region = [
            ('원주', '원주시'), ('춘천', '춘천시'), ('강릉', '강릉시'), ('동해', '동해시'),
        ]
    elif first_region == '경북':
        two_region = [
            ('포항', '포항시'), ('경주', '경주시'), ('김천', '김천시'), ('안동', '안동시'),
        ]
    else:
        two_region = [
            ('선택없음', '시, 도를 먼저 선택해주세요'),
        ]
'''
