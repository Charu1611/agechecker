from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    if request.method == 'POST':
        search = request.POST['abcd']
        print(search)
        url = 'https://api.agify.io?name='+search.replace(" ", "")
        print(url)
        apidata = requests.get(url).json()
        print(apidata)
        return render(request, 'index.html', {'apidata':apidata})
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['abcd']
        print(search)
        url = 'https://api.agify.io?name='+search.replace(" ", "")
        print(url)
        apidata = requests.get(url).json()
        print(apidata)
        return render(request, 'index.html', {'apidata':apidata})
    return render(request, 'search.html')

   