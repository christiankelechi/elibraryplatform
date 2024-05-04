from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    
# class BookSummarizeForm(forms.Form):
#     book_file=forms.FileField(max_length=5000)