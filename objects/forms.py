from django import forms
from .models import Error, Object, Documents, Lpu
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


class LpuForm(forms.ModelForm):

    class Meta:
        model = Lpu
        fields =('name','phone','img')


class ObjectForm(forms.ModelForm):

    lpu = forms.ModelChoiceField(queryset=Lpu.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Object
        fields = ('lpu', 'name', 'phone', 'project')