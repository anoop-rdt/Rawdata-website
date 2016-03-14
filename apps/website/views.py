from django.views import generic
from forms import ContactForm
from django.template import loader
from django.conf import settings
from django.http import HttpResponse
from html2text import html2text


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
    	context = super(HomePage, self).get_context_data(**kwargs)
        context['home_page'] = True
        return context


class ContactUsPage(generic.TemplateView):
    template_name = "contact-us.html"

    def get_context_data(self, **kwargs):
        context = super(ContactUsPage, self).get_context_data(**kwargs)
        contact_form = ContactForm(self.request.POST or None)
        context["contact_form"] = contact_form
        return context


class PythonDjangoPage(generic.TemplateView):
    template_name = "python-django.html"


class JavascriptPage(generic.TemplateView):
    template_name = "javascript.html"


class CrossPlatformPage(generic.TemplateView):
    template_name = "cross-platform.html"


class CustomerSuccessPage(generic.TemplateView):
    template_name = "customer_success.html"


class WhoweServePage(generic.TemplateView):
    template_name = "whoweserve.html"


def customer_contact(request):
	contact_form = ContactForm(request.POST)
	if contact_form.is_valid():
		context = {
					'contact_name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ':form.cleaned_data['contact_name'],
					'contact_email':form.cleaned_data['contact_email'],
					'contact_phone':form.cleaned_data['contact_phone'],
					'subject':form.cleaned_data['subject'],
					'content':form.cleaned_data['content']
				}
		body = loader.render_to_string('contact_email.html', context).strip()
		html_message = form.cleaned_data['content']
	   	message = html2text(html_message)
		send_mail(form.cleaned_data['subject'], message, form.cleaned_data['contact_email'] ,settings.FROM_DEFAULT_EMAIL, html_message=html_message)
		response = HttpResponse(status=200)
	else:
		response = HttpResponse(status=400)
		return response