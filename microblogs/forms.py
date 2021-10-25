from django import forms
from .models import User, Post
from django.core.validators import RegexValidator
from django.utils import timezone

class LogInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = {'bio': forms.Textarea() }


    password = forms.CharField(label='Password', widget=forms.PasswordInput(), validators=[RegexValidator(regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
    message='Password must be an uppercase character, lowercase character and a number'      )])
    password_confirmation = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password!')

    def save(self):
        super().save(commit=False)
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            bio=self.cleaned_data.get('bio'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
        )
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        widgets = {'text': forms.Textarea()}

    def save(self,user):
        super().save(commit=False)
        post = Post.objects.create(
            author=user,
            text = self.cleaned_data.get('text'),
            created_at = timezone.now()
        )
        return post