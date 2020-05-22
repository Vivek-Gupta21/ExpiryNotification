from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from ProductExpiryNotification.models import UserProfile, Product


class RegistrationForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",
                                                                        'placeholder': 'Confirm Password',
                                                                        'type': 'password',
                                                                        'id': 'password'
                                                                        }))
    contact_no = forms.CharField(required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Contact Number',
                                                               'type': 'tel',
                                                               'pattern': '[0-9].{4,}'
                                                               }))
    profile_pic = forms.CharField(required=False,
                                  widget=forms.FileInput(attrs={'class': 'input-group input-group-prepend '
                                                                         'form-control btn '
                                                                         'btn-sm btn-default',
                                                                }))
    notify_by = forms.ChoiceField(choices=UserProfile.NotificationTypes.choices)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First Name',
                                                 'type': 'text',
                                                 'id': 'first'
                                                 }),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Last Name',
                                                'type': 'text',
                                                'id': 'last'
                                                }),
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username',
                                               'type': 'text',
                                               'id': 'username'
                                               }),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'E-Mail',
                                            'type': 'email',
                                            'id': 'E-Mail'
                                            }),
            'password': forms.PasswordInput(attrs={'class': "form-control",
                                                   'placeholder': 'Password',
                                                   'type': 'password',
                                                   'id': 'repeat_password'
                                                   })
        }

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        repeat_password = all_clean_data['repeat_password']

        if password != repeat_password:
            print("Password don't match")
            self.add_error('password', forms.ValidationError('Passwords must match!'))
            self.add_error('repeat_password', forms.ValidationError(''))

    def clean_contact_no(self):
        contact_no = self.cleaned_data['contact_no']
        try:
            if int(contact_no) and not contact_no.isalpha():
                min_length = 8
                max_length = 13
                ph_length = str(contact_no)
                if len(ph_length) < min_length or len(ph_length) > max_length:
                    raise forms.ValidationError('Phone number length not valid')

        except (ValueError, TypeError):
            raise forms.ValidationError('Please enter a valid phone number')
        return contact_no


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",
                                                             'placeholder': 'Username',
                                                             'type': 'text'
                                                             }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",
                                                                 'placeholder': 'Password',
                                                                 'type': 'password'
                                                                 }))
    """
        #Add new arguments to kwargs.
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.username = username
    """


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'best_before', 'description', 'manufactured_date', 'notification_date',
                  'expiry_date']
        widgets = {
            'product_name': forms.TextInput(attrs={"class": "form-control",
                                                   "placeholder": "Product Name",
                                                   "type": "text"
                                                   }),
            'description': forms.TextInput(attrs={"class": "form-control",
                                                  "placeholder": "Product Description",
                                                  "type": "text"
                                                  }),
            'best_before': forms.TextInput(attrs={"class": "form-control",
                                                  "placeholder": "Best Before(Days)",
                                                  "type": "text"
                                                  }),
            'manufactured_date': forms.DateInput(attrs={"class": "form-control",
                                                        "placeholder": "Manufacturing Date",
                                                        "type": "date"
                                                        }),
            'expiry_date': forms.DateInput(attrs={"class": "form-control",
                                                  "placeholder": "Expiry Date",
                                                  "type": "date"
                                                  }),
            'notification_date': forms.DateInput(attrs={"class": "form-control",
                                                        "placeholder": "Notification Date",
                                                        "type": "date"
                                                        }),

        }
