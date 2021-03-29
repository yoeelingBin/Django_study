from django.shortcuts import render, get_object_or_404
from .models import Board


# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def about(request):
    return render(request, 'about.html')


def about_company(request):
    return render(request, 'about_company.html',
                  {'company_name': 'Simple Complex'})



def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board':board})
