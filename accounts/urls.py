from django.conf.urls import url, include
from accounts.views import logout, login, registration, profile, payment
from accounts import url_reset


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="register"),
    url(r'^profile', profile, name="profile"),
    url(r'^payment', payment, name="payment"),
    url(r'^password-reset/', include(url_reset)
    )
]