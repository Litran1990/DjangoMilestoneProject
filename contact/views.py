from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    """Returns a contact form"""

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['reason']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['description']
            try:
                send_mail(subject, message, from_email,
                          ['footballmuseum1999@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_sent')
    return render(request, 'contact.html', {'form': form})


def contact_sent(request):
    """
    Returns a page that confirms the contact
    form has been filled out and sent
    """

    return render(request, 'contact_sent.html')
