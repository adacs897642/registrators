from django import forms
from .models import Error, Object, Documents
from tzlocal import get_localzone


class ErrorsForm(forms.ModelForm):
    local_tz = get_localzone()
    obj = forms.ModelChoiceField(queryset=Object.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Error
        fields = ('obj','name', 'error')


class DocumentForm(forms.ModelForm):

    obj = forms.ModelChoiceField(queryset=Object.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Documents
        fields = ('obj','name','file')