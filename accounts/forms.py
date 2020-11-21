from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    """user signup form"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    """user login form"""
    model = get_user_model()
