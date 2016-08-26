from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView


"""
    Legacy code, I thought I shoudn't use Django Rest Framework for auth
"""


class LoginView(FormView):
    """
    This is a class based version of django.contrib.auth.views.login.
    Usage:
        in urls.py:
            url(r'^login/$',
                LoginView.as_view(
                    form_class=MyCustomAuthFormClass,
                    success_url='/my/custom/success/url/),
                name="login"),
    """
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('home')


class LogoutView(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self):
        logout(self.request)
        return reverse_lazy('home')