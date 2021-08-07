from django.forms import ModelForm
from .models import *


class MemberForm(ModelForm):
    class Meta:
        model = Member
        # fields = ['customer','product']
        fields = '__all__'
        exclude = ['registertime']