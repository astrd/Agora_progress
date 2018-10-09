from django.shortcuts import render
# from .models import Post
# Create your views here.

topics = [
    {
        'author': 'Miguel Cervantes',
        'title': 'Quijote',
        'content': 'So far so good',
        'date': 'October 2, 2018'
    },
    {
        'author': 'Tina Fey',
        'title': 'Mean Girls',
        'content': 'On Wednesdays we wear pink',
        'date': 'October 3, 2018'
    }
]
def home(request):
    context = { 'topics':topics}
    return render(request, 'agora/base.html', context)

def archive(request):
    return render(request, 'agora/archive.html', {'title': 'Archive'})