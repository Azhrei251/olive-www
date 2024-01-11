import sys

from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.views import generic
from django.utils.decorators import method_decorator
from basicauth.decorators import basic_auth_required
from web.settings import DEFAULT_FROM_EMAIL, SLACK_WEBHOOK_URL, SLACK_ICON
from .forms import ContactForm
from .models import View
import json
import requests


def index_view(request):
    if request.method == "GET":
        form = ContactForm()
        increment_visitor(request)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            slack_message = "Email: " + form.cleaned_data["email"] + "\nName: " + form.cleaned_data["name"] + "\nMessage: " + \
                      form.cleaned_data["message"]

            send_slack_notif(slack_message)
            name = form.cleaned_data["name"]
            contact_email = form.cleaned_data["email"]
            body = form.cleaned_data['message']
            body = "New contact from " + name + " [" + contact_email + "]" + "\n\n-----------------\n\n" + body
            subject = "Contact request: " + name
            try:
                message = EmailMultiAlternatives(
                    subject=subject,
                    body=body,
                    from_email=DEFAULT_FROM_EMAIL,
                    to=[DEFAULT_FROM_EMAIL],
                    reply_to=[contact_email]
                )
                message.send()
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "index.html", {"form": form})


def send_slack_notif(message):
    title = f"New contact :zap:"
    slack_data = {
        "username": "Azhapps Contact Bot",
        "icon_emoji": SLACK_ICON,
        "channel": "ob-contacts",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return redirect("success")


def success_view(request):
    return render(request, "success.html", {})


@method_decorator(basic_auth_required, name='get')
class VisitorView(generic.ListView):
    model = View
    template_name = 'visitors.html'
    queryset = View.objects.all()
    context_object_name = 'views'

    def get_context_data(self, **kwargs):
        context = super(VisitorView, self).get_context_data(**kwargs)
        context['total_views'] = self.queryset.count()
        return context


def increment_visitor(request):
    ip = get_client_ip(request)
    view = View.objects.get_or_create(ip_address=ip)
    view[0].count += 1
    view[0].save()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
