from django.conf.urls import url
from.views import contact, contact_sent

urlpatterns = [
    url(r'^contact-us/', contact, name="contact"),
    url(r'^success/', contact_sent, name="contact_sent"),
]