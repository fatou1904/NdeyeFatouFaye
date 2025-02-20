from django import forms
from django.contrib.auth.forms import UserCreationForm
from utilisateur.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Prénom')
    last_name = forms.CharField(max_length=100, required=True, label='Nom')
    email = forms.EmailField(required=True, label='Adresse email')
    profile_picture = forms.ImageField(required=False, label='Photo de profil')
    role = forms.ChoiceField(choices=CustomUser.CHOIX_ROLE, required=True, label="Rôle")

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'role', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    role = forms.ChoiceField(choices=CustomUser.CHOIX_ROLE, required=True, label="Rôle")

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
