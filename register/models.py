from django.db import models
from django.db.models import Model
from django.core.validators import EmailValidator
from django.core.validators import RegexValidator
from django.db.models.deletion import SET_NULL


class State(models.Model):
    state = models.CharField(max_length=225)

    def __str__(self):
        return self.state


class College(models.Model):
    College = models.CharField(max_length=225)

    def __str__(self):
        return self.College

    class Meta:
        ordering = ('College',)


YearOfGraduation_CHOICES = (
    ("1", "2022"),
    ("2", "2023"),
    ("3", "2024"),
    ("4", "2025"),
    ("5", "2026"),
    ("6", "2027"),

)
Study_Year_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),

)
Category_CHOICES = (
    ("Architecture", "Architecture"),
    ("Interior Design", "Interior Design"),
)
phone_regex = RegexValidator(regex=r'^\+?1?\d{10,10}$',
                             message="Phone must be in the format: '+999999999'.Please enter 10 digits mobile number.")


class RegisterForm(models.Model):
    uuid = models.CharField(null=True, max_length=10)
    Name = models.CharField(max_length=225)
    E_Mail = models.EmailField(validators=[EmailValidator(message="Check you Email")], verbose_name="E Mail")
    Phone = models.CharField(unique=True, max_length=10)
    states = models.ForeignKey(
        State, on_delete=models.CASCADE, default=1, verbose_name="State")
    Study_Year = models.CharField(choices=Study_Year_CHOICES, max_length=100, verbose_name="Study Year")
    College = models.ForeignKey(
        College, on_delete=models.CASCADE, default=1)
    Year_of_Graduation = models.CharField(choices=YearOfGraduation_CHOICES, max_length=100,
                                          verbose_name="Year of Graduation")
    Category = models.CharField(max_length=225, choices=Category_CHOICES)
    Date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


def user_directory_path_for_presentation(instance, filename):
    return 'projects/{0}_Presentation'.format(instance.uuid.uuid)


def user_directory_path_for_statement(instance, filename):
    return 'projects/{0}_Statement'.format(instance.uuid.uuid)


def user_directory_path_for_concept(instance, filename):
    return 'projects/{0}_Concept'.format(instance.uuid.uuid)


def user_directory_path_for_photo(instance, filename):
    return 'projects/{0}_Photo'.format(instance.uuid.uuid)


def user_directory_path_for_rendering(instance, filename):
    return 'projects/{0}_Rendering'.format(instance.uuid.uuid)


class upload(models.Model):
    uuid = models.ForeignKey(RegisterForm, on_delete=SET_NULL, null=True)
    form_1 = models.FileField(upload_to=user_directory_path_for_presentation, null=True)  # Presentation
    form_2 = models.FileField(upload_to=user_directory_path_for_statement, null=True)  # Design statement
    form_3 = models.FileField(upload_to=user_directory_path_for_concept,
                              null=True)  # Name and Theme Concept of the project
    form_4 = models.ImageField(upload_to=user_directory_path_for_photo, null=True, blank=True)  # Photograph
    form_5 = models.FileField(upload_to=user_directory_path_for_rendering, null=True,
                              blank=True)  # illustration/rendering

    def __str__(self):
        return f"{self.uuid}" if self.uuid else "no-uuid"