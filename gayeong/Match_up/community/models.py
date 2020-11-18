from django.db import models
from django.conf import settings
from account.models import *

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.")
    num_hit = models.PositiveIntegerField(default = 0)
    

    def __str__(self):
        return self.name

class TimeDate(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True

class Community_Post(TimeDate):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE) # 작성자
    title = models.CharField(max_length=200)
    title_image = models.ImageField(upload_to = 'image', blank=True)
    content = models.TextField()
    #하나의 글을 여러가지의 분류에 해당될 수 있다.(ex:정보, 유머), 하나의 분류에는 여러가지 글이 포함될 수 있죠.(정보 카테고리에 글 10개)
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요.")

    def __str__(self):
        return self.title

    #1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)]).py

    def is_title_more11(self):
        return len(self.title) > 11
    
    def get_title_under11(self):
        return self.title[:11]