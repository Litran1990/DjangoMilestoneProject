from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, billing_info
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="register"),
    url(r'^user_profile', user_profile, name="user_profile"),
    url(r'^billing_info', billing_info, name="billing_info"),
    url(r'^password-reset/', include(url_reset))
]