from cgitb import text
from tkinter import Widget
from typing import Text
from django import forms

class HashForm(forms.Form):
    text = forms.CharField(
        label="Enter hash here:",
        widget=forms.Textarea
    )