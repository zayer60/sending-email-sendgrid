from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.views.generic.edit import FormView
from django.views import View




class ContactView(FormView):
    template_name = 'emailapp/form.html'
    form_class = ContactForm
    success_url = 'thanks/'

    def form_valid(self, form):
        recipients = [form.cleaned_data['To']]
        subject = form.cleaned_data['Subject']
        message = form.cleaned_data['Message']
        sender = 'zayerwali12@gmail.com'
        try:
            send_mail(subject, message, sender, recipients, fail_silently=True)
            return HttpResponse('success')
        except BadHeaderError:
            return HttpResponse('invalid header found')
        return super().form_valid(form)



