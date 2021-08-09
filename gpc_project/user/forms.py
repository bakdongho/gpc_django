from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from user.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        fields=('username','email','name')