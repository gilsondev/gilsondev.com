# -*- coding: utf-8 -*-

import bleach

from django import forms
from django.utils.translation import ugettext as _
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field

from sendgrid.message import SendGridEmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label=_(u"Seu nome"))
    email = forms.EmailField(label=_(u"Seu e-mail"))
    subject = forms.CharField(label=_(u"Qual assunto?"))
    message = forms.CharField(label=_(u"Mensagem"), widget=forms.Textarea)

    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Field('name', css_name='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('email', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('subject', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('message', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Submit('send', _(u"Enviar Mensagem"), css_class='btn-success'),
            css_class='form-group text-center'
        )
    )


    def send(self):
        """Envia a mensagem para o e-mail
        configurado no projeto.
        """

        # Tratando conteudo para evitar conteudo maliciosos
        self.cleaned_data['message'] = bleach.clean(
            self.cleaned_data.get('message'),
            tags=settings.ALLOWED_TAGS,
            attributes=settings.ALLOWED_ATTRIBUTES,
            strip_comments=True,
        )

        mail_settings = {
            'subject': self.cleaned_data.get('subject'),
            'body': self.cleaned_data.get('message'),
            'from_email': self.cleaned_data.get('email')
        }
        email = SendGridEmailMessage(to=[settings.DEFAULT_FROM_EMAIL],
                                     **mail_settings)
        email.sendgrid_headers.setCategory("Contact")
        response = email.send()

        return response

