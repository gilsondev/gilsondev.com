# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy


from .forms import ContactForm


class ContactView(FormView):
    """View responsável pela página
    de contato do site.
    """
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        """Método sobrescrito para
        efetuar o envio da mensagem
        para o e-mail
        """
        form.send()
        return super(ContactView, self).form_valid(form)
