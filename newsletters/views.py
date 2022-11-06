from django.contrib import messages
from django.shortcuts import render
from .forms import NewsLetterUserSignUpForm
from newsletters.models import NewsLetterUser
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage


def newsletter_signup(request):
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.warning(request,'Este mail ya está registrado.')

        else:
            instance.save()
            messages.success(request,'Te hemos enviado un correo a tu bandeja de entrada.')
            #correo electrónico
            subject = "Libro de programación"
            from_email=settings.EMAIL_HOST_USER
            to_email=[instance.email]

            html_template='newsletters/email_templates/welcome.html'
            html_message=render_to_string(html_template)
            message=EmailMessage(subject,html_message,from_email,to_email)
            message.content_subtype = 'html'
            message.send()
        

    context= {
    'form':form,

    }

    return render(request,'start-here.html',context)


def newsletter_unsubscribe(request):
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exist():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,'Tu mail ha sido removido de nuestra base de datos.')

        else:
            print('Correo no encontrado.')
            messages.warning(request,'Correo no encontrado.')

    context={
        'form':form,
    }

    return render(request,'unsubscribe.html', context)