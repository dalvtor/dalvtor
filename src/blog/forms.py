from django import forms
from django.utils.translation import gettext as _


class PostSearchForm(forms.Form):
    q = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Search')}),
        required=False
    )
