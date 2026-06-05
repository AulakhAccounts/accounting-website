from django import forms
 
from .models import (
    ITRRequest,
    GSTRequest,
    TDSRequest,
    BookkeepingRequest
)
 
 
class StyledFormMixin:
 
    def apply_style(self):
 
        for field_name, field in self.fields.items():
 
            field.widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })
 
 
# ITR FORM
class ITRRequestForm(forms.ModelForm):
 
    class Meta:
 
        model = ITRRequest
 
        fields = '__all__'
 
        exclude = ['status', 'created_at']
 
    def __init__(self, *args, **kwargs):
 
        super().__init__(*args, **kwargs)
 
        StyledFormMixin.apply_style(self)
    def clean_phone(self):
 
        phone = self.cleaned_data['phone']
 
        if not phone.isdigit():
 
            raise forms.ValidationError(
                "Phone number must contain only digits."
            )
 
        if len(phone) != 10:
 
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )
 
        return phone
 
# GST FORM
class GSTRequestForm(forms.ModelForm):
 
    class Meta:
 
        model = GSTRequest
 
        fields = '__all__'
 
        exclude = ['status', 'created_at']
 
    def __init__(self, *args, **kwargs):
 
        super().__init__(*args, **kwargs)
 
        StyledFormMixin.apply_style(self)
    def clean_phone(self):
 
        phone = self.cleaned_data['phone']
 
        if not phone.isdigit():
 
            raise forms.ValidationError(
                "Phone number must contain only digits."
            )
 
        if len(phone) != 10:
 
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )
 
        return phone
 
# TDS FORM
class TDSRequestForm(forms.ModelForm):
 
    class Meta:
 
        model = TDSRequest
 
        fields = '__all__'
 
        exclude = ['status', 'created_at']
 
    def __init__(self, *args, **kwargs):
 
        super().__init__(*args, **kwargs)
 
        StyledFormMixin.apply_style(self)
    def clean_phone(self):
 
        phone = self.cleaned_data['phone']
 
        if not phone.isdigit():
 
            raise forms.ValidationError(
                "Phone number must contain only digits."
            )
 
        if len(phone) != 10:
 
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )
 
        return phone
 
# BOOKKEEPING FORM
class BookkeepingRequestForm(forms.ModelForm):
 
    class Meta:
 
        model = BookkeepingRequest
 
        fields = '__all__'
 
        exclude = ['status', 'created_at']
 
    def __init__(self, *args, **kwargs):
 
        super().__init__(*args, **kwargs)
 
        StyledFormMixin.apply_style(self)
    def clean_phone(self):
 
        phone = self.cleaned_data['phone']
 
        if not phone.isdigit():
 
            raise forms.ValidationError(
                "Phone number must contain only digits."
            )
 
        if len(phone) != 10:
 
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )
 
        return phone    
    
class ContactForm(forms.Form):
 
    full_name = forms.CharField(
 
        max_length=100,
 
        widget=forms.TextInput(
 
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }
        )
    )
 
 
    email = forms.EmailField(
 
        widget=forms.EmailInput(
 
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }
        )
    )
 
 
    message = forms.CharField(
 
        widget=forms.Textarea(
 
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5
            }
        )
    )