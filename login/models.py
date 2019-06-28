from django.db import models


# Create your models here.

# 继承models.Model,固定写法.创建两个字段,最大长度32位,char类型
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
