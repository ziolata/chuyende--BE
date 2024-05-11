from .models import UserCustom
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserCustom
        fields = ('email',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserCustom
        fields = ('email',)