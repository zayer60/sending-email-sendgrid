from django import forms


class ContactForm(forms.Form):
    To = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    Subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))



