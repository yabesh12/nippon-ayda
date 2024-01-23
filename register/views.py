import os
import random, string

from django.forms.utils import ErrorDict
from django.http import request
from ayda_registeration.settings import get_bool_from_env
from register.forms import reg_form, log_gorm, upload_form
from django.shortcuts import redirect, render
from register.models import RegisterForm, upload
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags, format_html_join
from django.shortcuts import reverse


def only_error_message(form_errors):
    return format_html_join(' ', '<li>{}</li>', form_errors.values())


# Create your views here.
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def fun(request):
    closed = get_bool_from_env('REGISTRATION_CLOSED', False)
    if closed:
        return render(request, "show.html", {'message': "Registration is closed"})
    message = {}
    if request.method == 'POST':
        form = reg_form(request.POST)
        if form.is_valid():
            uuid = id_generator()
            form.save()
            phone = form.cleaned_data['Phone']
            inst = RegisterForm.objects.get(Phone=phone)
            inst.uuid = uuid
            inst.save()
            subject = 'Thank you for registering'
            html_message = render_to_string('mail.html', {'context': uuid})
            plain_message = strip_tags(html_message)
            from_email = os.environ.get('FROM_EMAIL')
            to = form.cleaned_data['E_Mail']
            try:
                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                return render(request, "show.html", {'message': "Your registration is completed. Your ID is " + str(
                    uuid) + ". Use this ID for submission"})
            except:
                return render(request, "show.html", {'message': "fail To send E-mail"})
        else:
            return render(request, "show.html", {"message": "Mobile Number already exist"})
    form = reg_form()
    return render(request, "home.html", {'form': form})


def login(request):
    closed = get_bool_from_env('SUBMISSION_CLOSED', False)
    if closed:
        return render(request, "show.html", {'message': "Submission is closed"})
    if request.method == 'POST':
        form = log_gorm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('mobile_number')
            id = form.cleaned_data.get('registration_ID')
            if RegisterForm.objects.filter(Phone=phone, uuid=id).exists():
                inst = RegisterForm.objects.get(Phone=phone)
                request.session['user_id'] = inst.pk
                request.session['E-mail'] = inst.E_Mail
                if upload.objects.filter(uuid=inst):
                    return render(request, "login.html",
                                  {'form': form, 'error': "Already Submitted"})
                form = upload_form()
            else:
                form = log_gorm()
                return render(request, "login.html",
                              {'form': form,
                               'error': "Enter your correct registered Mobile Number and Registration ID"})
            return render(request, "upload.html", {"Name": inst.Name,
                                                   "E_Mail": inst.E_Mail,
                                                   "Phone": inst.Phone,
                                                   "states": inst.states,
                                                   "Study_Year": inst.Study_Year,
                                                   "College": inst.College,
                                                   "Year_of_Graduation": inst.get_Year_of_Graduation_display(),
                                                   "Category": inst.Category, "form": form})

    form = log_gorm()
    return render(request, "login.html", {'form': form})


def upload_view(request):
    closed = get_bool_from_env('SUBMISSION_CLOSED', False)
    if closed:
        return render(request, "show.html", {'message': "Submission is closed"})
    id = request.session.get('user_id')
    E_Mail = request.session.get('E-mail')
    print("2nd mail id {}".format(E_Mail))
    if request.method == 'POST':
        form = upload_form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.uuid_id = id
            data.save()
            subject = 'Thank you for submitting'
            html_message = render_to_string('mail_1.html')
            plain_message = strip_tags(html_message)
            from_email = os.environ.get('FROM_EMAIL')
            to = E_Mail
            try:
                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                try:
                    del request.session['id']
                    del request.session['E_Mail']
                except:
                    pass
                return render(request, "show.html", {'message': "You have successfully submitted."})
            except:
                return render(request, "show.html", {'message': "fail To send E-mail"})
        s = only_error_message(form_errors=form.errors)
        print(s)
        print(form.errors)
        return render(request, "show.html", {'message': s})
    return render(request, "show.html", {'message': "Sorry something went wrong"})
