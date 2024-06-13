from django import forms

class CreateLessonForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput({"class":"form-control"}))