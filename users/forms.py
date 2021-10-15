"""User Forms."""

# Django
from users.models import Profile
from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    """Signup form."""

    username = forms.CharField(
        min_length=4,
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder':'Nombre de usuario', 'class':'form-control', 'required': True}
        ),
    )
    password = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={'placeholder':'Escribe tu contraseña', 'class': 'form-control', 'required': True}
        ),
    )
    password_confirmation = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={'placeholder':'Repita su contraseña', 'class': 'form-control', 'required': True}
        ),
    )
    first_name = forms.CharField(
        min_length=2, 
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder':'Nombres', 'class': 'form-control', 'required': True}
        ),
    )
    last_name = forms.CharField(
        min_length=2, 
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder':'Apellidos', 'class': 'form-control', 'required': True}
        ),
    )
    email = forms.CharField(
        min_length=6, 
        max_length=70,
        widget=forms.EmailInput(attrs={'placeholder':'Correo Electronico', 'class': 'form-control', 'required': True}
        ),
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data
    
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile.objects.create(user=user)


# class ProfileForm(forms.Form):
#     """Profile form."""

#     website = forms.URLField(max_length=200, required=False)
#     biography = forms.CharField(max_length=500, required=True)
#     phone_number = forms.CharField(max_length=15, required=False)
#     picture = forms.ImageField()

class ProfileForm(forms.ModelForm):
    """Profile form."""

    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    picture = forms.ImageField()

    class Meta:
        """Form settings."""

        model = Profile
        fields = ['website', 'biography', 'phone_number', 'picture']