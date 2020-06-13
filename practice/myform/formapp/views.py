from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'formapp/index.html')

def MyForm(request):
    form = forms.MainForm()

    if request.method == 'POST':
        form = forms.MainForm(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE

            print('Validation Successful')
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])

    return render(request, 'formapp/myform.html', {'form':form})
