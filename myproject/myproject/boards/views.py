from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from django.contrib.auth.models import User


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


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first() # 获取现在登陆的用户

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        return redirect('board_topics', pk=board.pk) # 重定向回新建的topic页面

    return render(request, 'new_topic.html', {'board':board})
