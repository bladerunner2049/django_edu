import datetime
from django.db import models
from django.utils import timezone
from datetime import timedelta


# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Назва статті', max_length=200)
    article_text = models.TextField('Текст статті')
    pub_date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.article_title
    
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'


class Comment(models.Model):
    # Привязка комментів до статті
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Імя автора', max_length=50)
    comment_text = models.CharField('Текст коментарія', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'


class Subject(models.Model):
    subject_name = models.CharField(max_length=150, db_index=True, verbose_name='Назва предмету')
    subject_teacher = models.CharField('Викладач', max_length=100)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'
        #ordering = ['name']

class Test_case(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #test = models.ForeignKey(Test, on_delete=models.DO_NOTHING())
    case_name = models.CharField(max_length=100, verbose_name='Назва роботи', null=True)
    case_duration = models.IntegerField(default=10)

    def __str__(self):
        return self.case_name
    class Meta:
        verbose_name = 'Тестове завдання'
        verbose_name_plural = 'Тестові завдання'

class Test(models.Model):
    test_case = models.ForeignKey(Test_case, on_delete=models.CASCADE)
    sphere_id = models.CharField(max_length=50, verbose_name='ID завдання в sphere engine', null=True)
    attempts = models.IntegerField(verbose_name='Кількість спроб', default=1)

    def __str__(self):
        return self.sphere_id
    class Meta:
        verbose_name = 'Одиночне завдання'
        verbose_name_plural = 'Одиночні завдання'







#class Group(models.Model):
#    group_name = models.CharField('Назва групи', max_length=50)


"""class Student(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    #subject = models.ForeignKey(Subject)
   student_name = models.CharField("Ім'я студента", max_length = 100)"""
