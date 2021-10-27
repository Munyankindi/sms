from django.forms import ModelForm,fields
from .models import Stock

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
        