from django.db import models


class Company(models.Model):
    """
    Model-representation of any company
    """

    name = models.CharField(max_length=250, blank=False, unique=True, verbose_name='Название')
    address = models.CharField(max_length=250, blank=False, verbose_name='Адресс')
    foundation_date = models.DateField(blank=False, verbose_name='Дата создания')
    type = models.CharField(max_length=150, verbose_name='Тип')
    partners = models.ManyToManyField('self', verbose_name='Партнеры')

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'сompanies'

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    Model-representation of any role af an employee
    """

    name = models.CharField(max_length=250, blank=False, unique=True, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание')

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Model-representation of any employee in a company
    """

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    name = models.CharField(max_length=250, blank=False, verbose_name='Имя')
    age = models.PositiveSmallIntegerField(blank=False, verbose_name='Возраст')
    phone_number = models.CharField(max_length=30, unique=True, verbose_name='Номер телефона')
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES,
                              blank=False,
                              default=MALE,
                              verbose_name='Пол')
    role = models.ForeignKey(Role,
                             on_delete=models.CASCADE,
                             blank=False,
                             related_name='employees',
                             verbose_name='Профессия')
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                blank=False,
                                related_name='employees',
                                verbose_name='Компания')

    class Meta:
        ordering = ('name', '-age', )

    def __str__(self):
        return f"{self.name}, {self.age} лет"




