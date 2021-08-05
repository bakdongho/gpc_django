from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, Http404
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Article
# Create your views here.

def hello_world(request, to):
    return HttpResponse(f'hello {to}~!')

## CBV(Class Based View)
# 목록 보기
class ArticleListView(TemplateView):
    template_name='base.html'
    query_set= Article.objects.all()
    # template에 데이터 전달
    def get(self, request, *arg, **kwargs):
        ctx={
            'view' : self.__class__.__name__,
            'data' : self.query_set,
        }
        return self.render_to_response(ctx)

# 게시글 상세보기
class ArticleDetailView(TemplateView):
    template_name='base.html'
    query_set= Article.objects.all()
    pk_url_kwargs='article_id'

    def get_object(self, query_set=None):
        query_set= query_set or self.query_set
        pk = self.kwargs.get(self.pk_url_kwargs)
        return query_set.filter(pk=pk).first()

    def get(self, request, *arg, **kwargs):
        article=self.get_object()
        if not article:
            raise Http404('invalid article_id')
        ctx={
            'view' : self.__class__.__name__,
            'data' : article,
        }
        
        return self.render_to_response(ctx)


# 생성 및 수정
@method_decorator(csrf_exempt, name='dispatch')
class ArticleCreateUpdateView(TemplateView):  # 게시글 추가, 수정
    template_name = 'base.html'
    query_set= Article.objects.all()
    pk_url_kwargs='article_id'
    
    def get_object(self, query_set=None):
        query_set = query_set or self.query_set
        pk = self.kwargs.get(self.pk_url_kwargs)
        article=query_set.filter(pk=pk).first()
        if not article:
            raise Http404('invalid article_id')
        return article

    # 화면 요청
    def get(self, request, *args, **kwargs):  
        article = self.get_object()
        ctx = {
            'view': self.__class__.__name__,
            'data': article
        }
        return self.render_to_response(ctx)
    # 액션
    def post(self, request, *args, **kwargs): 
        action= request.POST.get('action')
        post_data={key:request.POST.get(key) for key in ('title', 'content','author')}
        for key in post_data:
            if not post_data[key]:
                raise Http404(f'no data for {key}')
        if action=='create':
            article=Article.objects.create(title=post_data['title'],
                                        content=post_data['content'],
                                        author=post_data['author'])
        elif action=='update':
            article = self.get_object()
            for key, value in post_data.items():
                setattr(article,key,value)
            article.save()
        else:
            raise Http404('invalid action')
        ctx = {
            'view' : self.__class__.__name__,
            'data' : article,
        }
        return self.render_to_response(ctx)
