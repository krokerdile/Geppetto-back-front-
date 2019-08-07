from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Comment
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
def board(request):
    boards=Board.objects.all().order_by('-id')
    return render(request, 'board.html',{'boards':boards})

def detail3(request, board_id):
    board_detail=get_object_or_404(Board, pk=board_id)

    user=request.user
    if board_detail.likes.filter(id=user.id):
        message="좋아요 취소"
    else:
        message="좋아요"

    return render(request, 'detail3.html',{'board':board_detail, 'message':message})

def new3(request):
    return render(request, 'new3.html')

def create3(request):
    board=Board()
    board.title=request.GET['title']
    board.writer=request.GET['writer']
    board.body=request.GET['body']
    board.pub_date=timezone.datetime.now()
    board.user=get_object_or_404(User, pk=request.GET['user_id'])
    board.save()

    return redirect('/board/'+str(board.id))

def edit3(request, board_id):
    board=get_object_or_404(Board, pk=board_id)
    return render(request, 'edit3.html',{'board':board})

def update3(request, board_id):
    board=get_object_or_404(Board, pk=board_id)
    board.title=request.GET['title']
    board.writer=request.GET['writer']
    board.body=request.GET['body']
    board.pub_date=timezone.datetime.now()
    board.save()

    return redirect('/board/'+str(board.id))

def delete3(request, board_id):
    board=get_object_or_404(Board, pk=board_id)
    board.delete()

    return redirect('board')

def comment_create(request, board_id):
    comment=Comment() # 댓글을 저장하기 위해 빈 Comment 객체를 하나 생성
    comment.body=request.GET['content'] # 댓글의 내용을 받아옴
    comment.board=get_object_or_404(Board, pk=board_id) # 해당 댓글을 어떤 blog 객체와 연결시켜 줄 것인지 찾아온다
    comment.save() # comment를 DB에 저장

    return redirect('/board/'+str(board_id))

def post_like(request, board_id):
    user = request.user # 로그인된 유저의 객체를 가져온다.
    board = get_object_or_404(Board, pk=board_id) # 좋아요 버튼을 누를 글을 가져온다.

    # 이미 좋아요를 눌렀다면 좋아요를 취소, 아직 안눌렀으면 좋아요를 누른다.
    if board.likes.filter(id=user.id): # 로그인한 user가 현재 blog 객체에 좋아요를 눌렀다면
        board.likes.remove(user) # 해당 좋아요를 없앤다.
    else: # 아직 좋아요를 누르지 않았다면
        board.likes.add(user) # 좋아요를 추가한다.

    return redirect('/board/' + str(board_id)) # 좋아요 처리를 하고 detail 페이지로 간다.