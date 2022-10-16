from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from web.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives


def index_view(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            contact_email = form.cleaned_data["email"]
            body = form.cleaned_data['message']
            body = "New contact from " + name + " [" + contact_email + "]" + "\n\n-----------------\n\n" + body
            subject = "Contact request: " + name
            try:
                messsage = EmailMultiAlternatives(
                    subject=subject,
                    body=body,
                    from_email=DEFAULT_FROM_EMAIL,
                    to=[DEFAULT_FROM_EMAIL],
                    reply_to=[contact_email]
                )
                messsage.send()
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "index.html", {"form": form})


def success_view(request):
    return render(request, "success.html", {})
