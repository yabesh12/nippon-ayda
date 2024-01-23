from register.models import RegisterForm, upload
from django import forms
from django.core.validators import ValidationError
from PIL import Image


class reg_form(forms.ModelForm):
    class Meta:
        model = RegisterForm
        exclude = ('uuid',)
        labels = {
            "Study_Year":"Year of study",
            "states": 'State Of College'
        }

    def clean_Phone(self):
        import re
        phone_regex_pattern = "^[6-9]\d{9}$"
        phone_regex = re.compile(phone_regex_pattern)

        mobile_number = self.cleaned_data['Phone']
        if len(str(mobile_number)) != 10 or not phone_regex.match(str(mobile_number)):
            raise ValidationError("Please enter a valid 10 digit mobile number.")
        return mobile_number
        


class upload_form(forms.ModelForm):
    class Meta:
        model = upload
        exclude = ('uuid',)
        labels = {'form_1': 'Presentation boards', 'form_2': 'Design Concept Statement',
                  'form_3': 'Name and Theme of Concept', 'form_4': 'Photograph',
                  'form_5': 'Labelling the Presentation Boards'}

    def clean_form_1(self):
        form_1 = self.cleaned_data['form_1']
        if form_1.size > 5000000:
            raise ValidationError('Presentation file must be 5MB or less!')
        return form_1

    # def clean_form_2(self):
    #     from_2 = self.cleaned_data['form_2']
    #     number_of_words = 0
    #     data = from_2.read()
    #     lines = data.split()
    #     number_of_words += len(lines)
    #     if number_of_words > 800:
    #         raise ValidationError('Design statement content must contain 800 words or less!')
    #     return from_2

    def clean_form_4(self):
        """Photograph """
        form_4 = self.cleaned_data['form_4']
        if form_4 is None:
            return form_4
        if form_4.content_type != 'image/jpeg':
            raise ValidationError('Photograph must be JPEG File format!')
        # img = Image.open(form_4)
        # dpi = img.info.get('dpi')
        # if not dpi:
        #     raise ValidationError('Please convert photo to 300 DPI and upload.')
        # if dpi != (300, 300):
        #     raise ValidationError('Photograph must be 300 DPI!, Please convert to 300 DPI and upload.')
        return form_4


class log_gorm(forms.Form):
    mobile_number = forms.IntegerField()
    registration_ID = forms.CharField()
