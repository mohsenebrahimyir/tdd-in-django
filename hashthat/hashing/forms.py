from cgitb import text
from tkinter import Widget
from typing import Text
from django import forms

class HashForm(forms.Form):
    text = forms.CharField(
        label="Entar hash here:",
        widget=forms.Textarea
    )