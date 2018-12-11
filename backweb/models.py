from django.db import models


# Create your models here.
class AType(models.Model):
    types = models.CharField(max_length=10)
    f_typeid = models.ForeignKey('self')

    class Meta:
        db_table = 'article_type'


class Article(models.Model):
    title = models.CharField(max_length=30, null=False)
    types = models.ForeignKey(AType, null=False, on_delete=models.CASCADE)
    is_show = models.BooleanField(default=False)
    is_recommend = models.BooleanField(default=False)
    desc = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=10000, null=True)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'article'


class User(models.Model):
    username = models.CharField(max_length=10, null=False)
    password = models.IntegerField(max_length=10, null=False)

    class Meta:
        db_table = 'user'