from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=256)
    desc = models.TextField(verbose_name='Специальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'


class Student(models.Model):
    surname = models.CharField(verbose_name='Фамилия', max_length=128)
    name = models.CharField(verbose_name='Имя', max_length=128)
    patronymic = models.CharField(verbose_name='Отчество', max_length=128, blank=True)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.surname} | {self.group}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

