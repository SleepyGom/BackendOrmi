from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView , CreateView, DetailView , UpdateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     # 나머지 요청
#     # 에러, 예외처리
#     return HttpResponse('NO!!!')


class Index(View):
    def get(self, request):
        # return HttpResponse('Index page GET class')

        # 데이터베이스에 접근해서 값을 가져와야한다
        # 게시판에 글들ㅇ르 보여줘야하기 떄문에 데이터베이스에서 "값 조회"
        # MyModel.objects.all()
        post_objs = Post.objects.all()
        # context = 데이터베이스에서 가져온 값
        context = {
            "posts" : post_objs
        }
        return render(request,'blog/board.html', context)
    

# write
# post - form
# 글 작성 화면
def write(request):
    if request.method == 'POST':
        # form 확인
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:list')
    else:
        form = PostForm()
        return render(request, 'blog/write.html', {'form': form})
    

# Django 자체의 클래스 뷰 기능도 강력, 편리
# django.vies.generic -> ListView
class List(ListView):
    model = Post # 모델
    template_name = 'blog/post_list.html' # 템플릿
    context_object_name = 'posts' # 변수 값의 이름


class Write(CreateView):
    model = Post # 모델
    form_class = PostForm # 폼
    success_url = reverse_lazy('blog:list') # 성공시 보내줄 url
    

class Detail(DetailView):
    model = Post # 모델
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class Update(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('bolg:list')
    # initial 기능
    def get_initial(self):
        initial = super().get_initial() # UpdateView(generic view) 에서 제공하는 initial(딕셔너리)
        post = self.get_object() # pk 기반으로 객체를 가져온다
        initial['title'] = post.title
        initial['content'] = post.content
        return initial