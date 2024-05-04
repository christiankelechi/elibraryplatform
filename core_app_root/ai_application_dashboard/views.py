import threading
import webbrowser
from django.shortcuts import render
import threading
from django.core.files.storage import FileSystemStorage
# Create your views here.
from . import extract_txt
from . import summarizetxt
import ast
from ast import literal_eval
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from .forms import SearchForm
from pycite.pycite import PyCite

def dashboard(request):
    return render(request,"dashboard/dashboard.html")

from django.shortcuts import render
from .forms import SearchForm
import webview
no_of_search=0
url=""
def open_search_view_results(url):
    webview.create_window('Search Results', url)
    webview.start()

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Fetch data from other sites using the query
            # url = 'https://google.com/search?q=' + query
            # url=url
            # no_of_search=1
            # no_of_search=no_of_search
            # webbrowser.open(url)
            return render(request, 'dashboard/search.html', {'form': form})
    else:
        form = SearchForm()
    return render(request, 'dashboard/search.html', {'form': form})

def fetch_search_results(query):
    # Example of fetching data from another site (modify this according to your needs)
    url = 'https://google.com/search?q=' + query
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract links from the fetched data
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links


def book(request):
    return render(request,'dashboard/books.html')

def recommendation(request):
    return render(request,'dashboard/recommendation.html')

def save_page(request):
    return render(request,'dashboard/save.html')

def summarize(request):
    if request.method == 'POST' and request.FILES['book_file']:
        uploaded_file = request.FILES['book_file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(filename)
        
        # Process the uploaded PDF file
        extract_txt.pdf_to_json(pdf_path=file_path, json_file="extracted_book_text.json")
        
        # Read the extracted text from the JSON file
        with open("extracted_book_text.json", "r") as f:
            pdf_text = f.read()
        
        pdf_text=summarizetxt.generate_summary(str(pdf_text))
        # Now you can do something with the extracted text
        # For example, you could render it in a template
        return render(request, 'dashboard/text-summariser.html', {'text': pdf_text})
    
    return render(request, 'dashboard/text-summariser.html',{'text':''})

def reference_generator(request):
    if request.method == 'POST':
        url_text = request.POST['url_of_site'] 
        with open("testlinks.txt","w") as file:
            file.write(url_text)
        # Assuming you have a form with input fields named 'urls'
        my_citations = PyCite(input_file="testlinks.txt",output_file='citations.txt')
        
        citations = my_citations.cite()
        # with open("citations","r") as readFile:
        #     citations
        return render(request, 'dashboard/reference-generator.html', {'citations': citations})

    return render(request,'dashboard/reference-generator.html')