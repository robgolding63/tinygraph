from django import forms
from tinygraph.apps.devices.models import Device
from django.db.models import Q
from django.template.defaultfilters import slugify

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ('data_objects', 'ip_address', 'fqdn', 'packages')
    
    def clean_user_given_name(self):
        user_given_name = self.cleaned_data['user_given_name']
        try:
            Device.objects.get(~Q(pk=self.instance.pk), slug=slugify(str(user_given_name)))
        except Device.DoesNotExist:
            return user_given_name
        else:
            raise forms.ValidationError('This name is too similar to another devices name.')