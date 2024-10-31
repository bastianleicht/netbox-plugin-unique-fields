from django.shortcuts import render
from dcim.models import Device
from .forms import DeviceCustomFieldForm


def device_create_view(request):
    if request.method == 'POST':
        form = DeviceCustomFieldForm(request.POST)
        if form.is_valid():
            device = form.save()
            # Zusätzliche Logik für das Speichern von Custom Fields in der Gerätedatenbank (falls erforderlich)
            return redirect('dcim:device', pk=device.pk)
    else:
        form = DeviceCustomFieldForm()

    return render(request, 'dcim/device_add.html', {'form': form})
