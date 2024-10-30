from django import forms
from utilities.forms import BootstrapMixin
from .models import RoleCustomFieldMapping


class RoleCustomFieldMappingForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = RoleCustomFieldMapping
        fields = ['custom_field', 'device_role', 'description']

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional validation here
        return cleaned_data