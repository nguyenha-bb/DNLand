from django import forms
from .models import Post, Province, District, Ward, Direction

class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'custom_widgets/custom_clearable_file_input.html'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'price', 'square', 'addressDetail', 'description', 'image', 'province', 'district', 'ward', 'direction']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Tiêu đề ...', 'oninput': 'clearErrorMessage()'}),
            'price': forms.TextInput(attrs={'placeholder': 'Giá ...', 'oninput': 'updateFormattedPrice()'}),
            'square': forms.TextInput(attrs={'placeholder': 'Diện tích ...', 'oninput': 'clearErrorMessage()'}),
            'addressDetail': forms.TextInput(attrs={'placeholder': 'Số nhà, tên đường ...', 'oninput': 'clearErrorMessage()'}),
            'description': forms.Textarea(attrs = {'placeholder': 'Mô tả ...', 'oninput': 'clearErrorMessage()'}),
            'image': CustomClearableFileInput(),
        }
    province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        to_field_name='id',
        required=True,  
        widget=forms.Select(attrs={'onchange': 'loadDistricts(this.value)'})
    )
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        to_field_name='id',
        required=True,  
        widget=forms.Select(attrs={'onchange': 'loadWards(this.value)', 'oninput': 'clearErrorMessage()'})
    )
    ward = forms.ModelChoiceField(
        queryset=Ward.objects.all(),
        to_field_name='id',
        required=True,  
        widget=forms.Select(attrs={'oninput': 'clearErrorMessage()'})
    )
    direction = forms.ModelChoiceField(
        queryset=Direction.objects.all(),
        to_field_name='id',
        required=True,  
        widget=forms.Select(attrs={'oninput': 'clearErrorMessage()'})
    )