from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateField
    is_published = models.BooleanField()
    category = models.ManyToManyField('Category')
    comments = models.ManyToManyField('Comments')
    likes = models.ForeignKey('Likes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Comments(models.Model):
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class Likes(models.Model):
    like = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'Лайки'


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    # image = models.ImageField(upload_to='users/%y/%m/%d', blank=True)
    # строка выше позволит хранить изображения в каталогах вида MEDIA_ROOT/users/2020/05/26
    def __str__(self):
        return self.title
