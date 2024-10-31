from django import forms
from dcim.models import Device
from .models import RoleCustomField

class DeviceCustomFieldForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'  # Alle Standardfelder des Geräts

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        device_role = self.instance.device_role if self.instance else None

        # Dynamisch Custom Fields basierend auf der Geräte-Rolle hinzufügen
        if device_role:
            role_fields = RoleCustomField.objects.filter(device_role=device_role)
            for field in role_fields:
                field_type = field.field_type
                if field_type == 'string':
                    self.fields[field.field_name] = forms.CharField(initial=field.field_default, required=False)
                elif field_type == 'integer':
                    self.fields[field.field_name] = forms.IntegerField(initial=field.field_default, required=False)
                elif field_type == 'boolean':
                    self.fields[field.field_name] = forms.BooleanField(initial=field.field_default, required=False)
