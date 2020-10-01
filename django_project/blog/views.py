from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'AAA',
        'title': 'BBB',
        'content': 'ccc',
        'date_posted': '11/11/11'
    },
    {
        'author': 'AAA',
        'title': 'BBB',
        'content': 'ccc',
        'date_posted': '11/11/11'
    },    {
        'author': 'AAA',
        'title': 'BBB',
        'content': 'ccc',
        'date_posted': '11/11/11'
    },
]


def home(request):
    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
