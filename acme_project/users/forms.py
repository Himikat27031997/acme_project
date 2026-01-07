from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:  # Наследуемся от Meta класса родителя
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'birthday')  # Добавляем новые поля


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
