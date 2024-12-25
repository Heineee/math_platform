from django.db import models

# Create your models here.

# username, password, email, gender, birthday, address, last_login, last_exit, pictureaddress
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50,primary_key=True)
    # 允许为空的性别
    gender = models.CharField(max_length=10, blank=True, null=True)
    # 允许为空的生日,默认为2000-01-01
    birthday = models.DateField(default='2000-01-01')
    # 允许为空的地址
    address = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)
    last_exit = models.DateTimeField(auto_now=True)
    pictureaddress = models.CharField(max_length=100, blank=True, null=True)
    class Meta:#  this is to define the name of the table in the database
        db_table = 'user-account'

# username, password, identify
class Admin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    identify = models.CharField(max_length=8,primary_key=True)

    class Meta:#  this is to define the name of the table in the database
        db_table = 'admin-account'

# title, text, username, pictureaddress, index, likes, dislikes, date, recommended_developer, viewers, Judge
class Posttext(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    username =models.CharField(max_length=20)# this is to create a foreign key relationship with the user table
    pictureaddress = models.CharField(max_length=100, blank=True, null=True)
    index= models.AutoField(primary_key=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    recommended_developer= models.BooleanField(default=False)
    viewers = models.IntegerField(default=0)
    Judge = models.BooleanField(default=False)
    class Meta:#  this is to define the name of the table in the database
        db_table = 'text'

    # def like_post(self):
    #     self.likes += 1  # 修改这里，每次点赞增加2
    #     self.save()
    # def dislike_post(self):
    #     self.dislikes += 1
    #     self.save()
    # def view_post(self):
    #     self.viewers += 1
    #     self.save()

# index,title,question
class Question(models.Model):
    index = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    question = models.TextField(max_length=1000)
    class Meta:
        db_table = 'question'

# index,username,question_title,answer,Judge
class Answer_question(models.Model):
    index = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    question_title = models.CharField(max_length=50)
    answer = models.TextField(max_length=1000)
    Judge = models.BooleanField(default=False)
    class Meta:#  this is to define the name of the table in the database
        db_table = 'answer_question'
