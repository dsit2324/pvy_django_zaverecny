from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # Poznámka pro vývojáře: formulář rozšiřuje výchozí Django registraci o email a Bootstrap stylování.
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        # Poznámka pro vývojáře: všechny prvky formuláře dostávají class="form-control" pro jednotný vzhled.
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })