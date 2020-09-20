from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
import requests
from newsapi import NewsApiClient
from .forms import SearchForm
newsapi = NewsApiClient(api_key='4aa081052e754088b9fa90f7f10ca1b1')
q = ""
# Create your views here.
def HomePage(request):
	
	# /v2/top-headlines
	top_headlines = newsapi.get_top_headlines(country='in',
											page_size = 10)
	articles = top_headlines["articles"]
	return render(request, "main/home.html", {'top_headlines': top_headlines})

def Search(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			q = data['q']

			#top_headlines = newsapi.get_top_headlines(q = q,
             #                         		language='en',
              #                        		country='in')
			#return HttpResponseRedirect('/result/', q)
			return redirect('result', query = q)
	else:
		form = SearchForm()
		top_headlines = newsapi.get_top_headlines(country='in',
											page_size = 10)
	return render(request, "main/search.html", {'form': form, 'top_headlines': top_headlines})

def Result(request, query):
	top_headlines = newsapi.get_top_headlines(q = query,language='en')
	print(query)
	print(top_headlines)
	return render(request, "main/home.html", {'top_headlines': top_headlines})
#class SearchResultsView(ListView):
#	template_name = 'search_results.html'