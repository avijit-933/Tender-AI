from django import forms
from .models import Tender
from django.core.exceptions import ValidationError


class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = [
            'tender_id', 'title', 'department', 'boq_file', 
            'min_turnover', 'min_experience', 'certificates', 'manpower',
            'weight_price', 'weight_experience', 'weight_technical', 'weight_performance',
            'last_date', 'required_documents', 'category'
        ]
        widgets = {
            'last_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        total_weight = (
            cleaned_data.get('weight_price', 0) +
            cleaned_data.get('weight_experience', 0) +
            cleaned_data.get('weight_technical', 0) +
            cleaned_data.get('weight_performance', 0)
        )
        if total_weight != 100:
            raise ValidationError("Total AI weight must be 100%")
        return cleaned_data

