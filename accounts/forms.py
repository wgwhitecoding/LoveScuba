from django import forms
from allauth.account.forms import SignupForm
from django_countries.fields import CountryField
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'age', 'country_of_origin', 'gender', 'diver_type']

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    age = forms.IntegerField(label='Age')
    country_of_origin = CountryField().formfield(label='Country of Origin')
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')
    DIVER_TYPE_CHOICES = [
        ('leisure', 'Leisure'),
        ('professional', 'Professional'),
    ]
    diver_type = forms.ChoiceField(choices=DIVER_TYPE_CHOICES, label='Diver Type', required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.profile.age = self.cleaned_data['age']
        user.profile.country_of_origin = self.cleaned_data['country_of_origin']
        user.profile.gender = self.cleaned_data['gender']
        user.profile.diver_type = self.cleaned_data['diver_type']
        user.profile.is_professional = (self.cleaned_data['diver_type'] == 'professional')
        user.save()
        user.profile.save()
        return user



